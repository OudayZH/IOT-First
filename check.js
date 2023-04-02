var firebaseConfig = {
    apiKey: "AIzaSyDx5chvzhHyyLSHAuIsQqAuR_xVP8KP95E",
    authDomain: "5jax8sTeAbBSgK60uwlYHcjx2igeobISNYLn92oS",
    databaseURL: "https://esp8266-dht11-60d2d-default-rtdb.firebaseio.com/",
    projectId: "esp8266-dht11-60d2d",

  };
  firebase.initializeApp(firebaseConfig);
  
  function checkAuthState() {
    firebase.auth().onAuthStateChanged(function(user) {
      if (user) {
        // user is signed in, allow access to the page
      } else {
        // user is not signed in, redirect to login page
        window.location.href = '/Log.html';
      }
    });
  }
  
  // Call checkAuthState when the page loads
  window.onload = function() {
    checkAuthState();
  };
  