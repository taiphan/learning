# Google Sign-In Setup (Firebase Auth)

The learning app uses **Firebase Authentication** (Google provider) and **Firestore** to sync progress across devices. Without configuration, progress stays in **localStorage** only (header shows **Local** pill).

---

## 1. Create Firebase project

1. [Firebase Console](https://console.firebase.google.com/) → **Add project**
2. Project settings → **Your apps** → **Web** (`</>`)
3. Copy the `firebaseConfig` object

---

## 2. Enable Google sign-in

1. **Build** → **Authentication** → **Get started**
2. **Sign-in method** → **Google** → Enable → set support email → Save

---

## 3. Authorized domains

**Authentication** → **Settings** → **Authorized domains** — add:

| Domain | Use |
|--------|-----|
| `localhost` | Local dev (`python3 -m http.server 8081`) |
| `taiphan.github.io` | GitHub Pages (no `https://`) |

> Error `auth/unauthorized-domain` = domain missing from this list.

---

## 4. Firestore database

1. **Build** → **Firestore Database** → Create database
2. Start in **production mode** (we add rules below)
3. **Rules** tab — paste from [`firestore.rules.example`](./firestore.rules.example) → Publish

Collection used: `learning_progress/{userId}`

---

## 5. App configuration

**Local development:**

```bash
cp apps/learning/auth-config.example.js apps/learning/auth-config.js
# Edit auth-config.js: paste firebase config, set enabled: true
```

**GitHub Pages (CI secrets):**

Add repository secrets (Settings → Secrets → Actions):

| Secret | Firebase config field |
|--------|------------------------|
| `FIREBASE_API_KEY` | apiKey |
| `FIREBASE_AUTH_DOMAIN` | authDomain |
| `FIREBASE_PROJECT_ID` | projectId |
| `FIREBASE_STORAGE_BUCKET` | storageBucket |
| `FIREBASE_MESSAGING_SENDER_ID` | messagingSenderId |
| `FIREBASE_APP_ID` | appId |

Deploy workflow writes `auth-config.js` when `FIREBASE_API_KEY` is set.

---

## 6. Verify

1. `cd apps/learning && python3 -m http.server 8081`
2. Open http://localhost:8081 — header **Sign in** or **Account** → opens `#auth` page
3. On the auth page, click **Sign in with Google** → toast **Progress synced with Google account**
4. Complete a week → check Firestore `learning_progress` document for your uid

**Auth page URL:** `https://taiphan.github.io/learning/#auth` (or `#account`)

---

## Behavior

| State | Progress storage |
|-------|------------------|
| Not signed in | `localStorage` only |
| Signed in | `localStorage` + Firestore merge on login & auto-sync on save |

**Merge on login:** union of completed weeks and Track B milestones; notes merged (local wins on same week key).

---

## Security notes

- Firebase **apiKey** is public in client apps — security comes from **Firestore rules** and **authorized domains**
- Never commit service account keys
- Rules: users can read/write **only** their own `learning_progress/{uid}` doc

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Button hidden, shows **Local** | `enabled: false` in auth-config.js or missing Firebase secrets on deploy |
| Popup closes instantly | Add domain to Authorized domains |
| Sync failed toast | Check Firestore rules and that database exists |
| Progress not merging | Sign out/in again; check browser console |
