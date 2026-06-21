/** Default: auth off until you copy auth-config.example.js or CI injects secrets. */
window.AUTH_CONFIG = {
  enabled: false,
  firebase: {
    apiKey: "",
    authDomain: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: "",
  },
};
