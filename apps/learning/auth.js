/**
 * Google sign-in (Firebase Auth) + optional Firestore progress sync.
 * Requires auth-config.js with enabled: true and valid firebase config.
 */
(function () {
  const cfg = window.AUTH_CONFIG || { enabled: false };
  let auth = null;
  let db = null;
  let user = null;
  let syncTimer = null;

  const $ = (sel) => document.querySelector(sel);

  function isConfigured() {
    if (!cfg.enabled) return false;
    const f = cfg.firebase || {};
    return Boolean(f.apiKey && f.projectId && f.authDomain);
  }

  function progressDocId(uid) {
    return uid;
  }

  function mergeProgress(local, remote) {
    const a = local || {};
    const b = remote || {};
    const weeks = [...new Set([...(a.completedWeeks || []), ...(b.completedWeeks || [])])].sort(
      (x, y) => x - y
    );
    const trackB = [...new Set([...(a.trackBCompleted || []), ...(b.trackBCompleted || [])])].sort(
      (x, y) => x - y
    );
    const currentWeek = Math.max(a.currentWeek || 1, b.currentWeek || 1, weeks.length ? Math.max(...weeks) : 1);
    const notes = { ...(b.notes || {}), ...(a.notes || {}) };
    return {
      completedWeeks: weeks,
      trackBCompleted: trackB,
      currentWeek: Math.min(52, currentWeek),
      notes,
      activeTab: a.activeTab || b.activeTab || "overview",
      syncedAt: new Date().toISOString(),
    };
  }

  async function loadRemoteProgress(uid) {
    if (!db) return null;
    const snap = await db.collection("learning_progress").doc(progressDocId(uid)).get();
    if (!snap.exists) return null;
    const d = snap.data();
    return {
      completedWeeks: d.completedWeeks || [],
      trackBCompleted: d.trackBCompleted || [],
      currentWeek: d.currentWeek || 1,
      notes: d.notes || {},
      activeTab: d.activeTab || "overview",
    };
  }

  async function pushProgress(uid, progress) {
    if (!db || !uid || !progress) return;
    await db
      .collection("learning_progress")
      .doc(progressDocId(uid))
      .set(
        {
          completedWeeks: progress.completedWeeks || [],
          trackBCompleted: progress.trackBCompleted || [],
          currentWeek: progress.currentWeek || 1,
          notes: progress.notes || {},
          activeTab: progress.activeTab || "overview",
          email: user?.email || null,
          displayName: user?.displayName || null,
          photoURL: user?.photoURL || null,
          updatedAt: firebase.firestore.FieldValue.serverTimestamp(),
        },
        { merge: true }
      );
  }

  function scheduleSync(progress) {
    if (!user || !db) return;
    clearTimeout(syncTimer);
    syncTimer = setTimeout(() => {
      pushProgress(user.uid, progress).catch((err) => {
        console.warn("Progress sync failed:", err);
        window.__learningToast?.("Could not sync progress — saved locally");
      });
    }, 800);
  }

  function renderAuthUI() {
    const signedIn = $("#authSignedIn");
    const signedOut = $("#authSignedOut");
    const localOnly = $("#authLocalOnly");
    if (!signedIn || !signedOut) return;

    if (!isConfigured()) {
      signedIn.hidden = true;
      signedOut.hidden = true;
      if (localOnly) localOnly.hidden = false;
      return;
    }
    if (localOnly) localOnly.hidden = true;

    if (user) {
      signedOut.hidden = true;
      signedIn.hidden = false;
      const img = $("#authPhoto");
      const name = $("#authName");
      if (img) {
        if (user.photoURL) {
          img.src = user.photoURL;
          img.alt = user.displayName || "User";
          img.hidden = false;
        } else {
          img.hidden = true;
        }
      }
      if (name) name.textContent = user.displayName || user.email || "Signed in";
    } else {
      signedIn.hidden = true;
      signedOut.hidden = false;
    }
  }

  async function signInWithGoogle() {
    if (!auth) {
      window.__learningToast?.("Sign-in not configured — see AUTH-SETUP.md");
      return;
    }
    const provider = new firebase.auth.GoogleAuthProvider();
    provider.setCustomParameters({ prompt: "select_account" });
    try {
      await auth.signInWithPopup(provider);
    } catch (err) {
      console.error(err);
      const msg =
        err.code === "auth/popup-closed-by-user"
          ? "Sign-in cancelled"
          : err.code === "auth/unauthorized-domain"
            ? "Domain not authorized in Firebase Console"
            : err.message || "Sign-in failed";
      window.__learningToast?.(msg);
    }
  }

  async function signOutUser() {
    if (!auth) return;
    try {
      await auth.signOut();
      window.__learningToast?.("Signed out — progress kept on this device");
    } catch (err) {
      window.__learningToast?.("Sign-out failed");
    }
  }

  async function onUserChanged(fbUser) {
    user = fbUser;
    renderAuthUI();
    if (!fbUser) return;

    const getLocal = window.__learningAuthGetProgress;
    const apply = window.__learningAuthApplyProgress;
    if (!getLocal || !apply) return;

    try {
      const remote = await loadRemoteProgress(fbUser.uid);
      const merged = mergeProgress(getLocal(), remote);
      apply(merged, { source: "cloud-merge" });
      await pushProgress(fbUser.uid, merged);
      window.__learningToast?.("Progress synced with Google account");
    } catch (err) {
      console.warn(err);
      window.__learningToast?.("Signed in — using local progress (sync unavailable)");
    }
  }

  function initFirebase() {
    if (!isConfigured()) {
      renderAuthUI();
      return;
    }
    if (typeof firebase === "undefined") {
      console.warn("Firebase SDK not loaded");
      return;
    }
    firebase.initializeApp(cfg.firebase);
    auth = firebase.auth();
    db = firebase.firestore();
    auth.onAuthStateChanged(onUserChanged);
    renderAuthUI();
  }

  function bindAuthEvents() {
    $("#googleSignInBtn")?.addEventListener("click", signInWithGoogle);
    $("#authSignOutBtn")?.addEventListener("click", signOutUser);
  }

  window.LearningAuth = {
    isConfigured,
    isSignedIn: () => Boolean(user),
    getUser: () => user,
    syncProgress: (progress) => {
      if (user) scheduleSync(progress);
    },
    signIn: signInWithGoogle,
    signOut: signOutUser,
    init: initFirebase,
  };

  bindAuthEvents();
  renderAuthUI();
})();
