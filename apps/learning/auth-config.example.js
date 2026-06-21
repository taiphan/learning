/**
 * Copy to auth-config.js and fill in your Firebase web app config.
 * Firebase Console → Project settings → Your apps → Web app.
 * Enable Google sign-in: Authentication → Sign-in method → Google.
 * Authorized domains: localhost, taiphan.github.io (no protocol/port).
 */
window.AUTH_CONFIG = {
  enabled: false,
  firebase: {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_PROJECT.firebaseapp.com",
    projectId: "YOUR_PROJECT_ID",
    storageBucket: "YOUR_PROJECT.appspot.com",
    messagingSenderId: "000000000000",
    appId: "1:000000000000:web:xxxxxxxx",
  },
};
