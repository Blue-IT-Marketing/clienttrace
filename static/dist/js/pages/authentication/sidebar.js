
  // Initialize Firebase
try{
var config =
{
    apiKey: "AIzaSyAFLmjXNDYFEMD4tCvCJJHhzsH0DMX5_xw",
    authDomain: "client-trace.firebaseapp.com",
    databaseURL: "https://client-trace.firebaseio.com",
    projectId: "client-trace",
    storageBucket: "client-trace.appspot.com",
    messagingSenderId: "169154514210"
};
if (!firebase.apps.length) {
    firebase.initializeApp(config);
}else {
}
}catch (err){

}

function initApp() {
  // Listening for auth state changes.
  // [START authstatelistener]
  firebase.auth().onAuthStateChanged(function(user) {
    // [START_EXCLUDE silent]

    // [END_EXCLUDE]
    if (user) {
      // User is signed in.
      var displayName = user.displayName;
      var email = user.email;
      var emailVerified = user.emailVerified;
      var photoURL = user.photoURL;
      var isAnonymous = user.isAnonymous;
      var uid = user.uid;
      var providerData = user.providerData;
      // [START_EXCLUDE]
      document.getElementById('strSideUserImageID').src =photoURL;
      document.getElementById('strSideUserNameID').textContent =displayName;

      if (!emailVerified) {
          var vstrChoice = 0;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
      }else
          {
          var vstrChoice = 0;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
          }
      // [END_EXCLUDE]
    } else
        {
      // User is signed out.
          var vstrChoice = 1;
          var dataString = "&vstrChoice=" + vstrChoice;
          $.ajax({
              type:"post",
              url: "/login",
              data: dataString,
              cache: false,
              success: function (SideBar) {
                  $('#SideBarMenu').html(SideBar);
              }
          })
    }
  });
}

initApp();

