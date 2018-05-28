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
var thisLogOutButton = document.getElementById("LogOutButton");
thisLogOutButton.addEventListener("click", signOut);
  function signOut()
  {
        firebase.auth().signOut().then(function() {
          console.log('Signed Out');
          alert("Successfully signed out");
          thisLogOutButton.disabled = true;
        }, function(error) {
          console.error('Sign Out Error', error);
        });
  }