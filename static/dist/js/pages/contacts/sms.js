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

function countChar(val) {
var len = val.value.length;
if (len >= 150) {
  val.value = val.value.substring(0, 150);
} else {
  $('#charNum').html("Character Limit = " + (150 - len));
}
}

var thisSendMessageButt = document.getElementById("SendMessageButt");
thisSendMessageButt.addEventListener("click", function () {
    firebase.auth().onAuthStateChanged(function (user) {
        if (user) {
            user.getIdToken().then(function (accessToken) {
                // User is signed in.
                var displayName = user.displayName;
                var email = user.email;
                var photoURL = user.photoURL;
                var isAnonymous = user.isAnonymous;
                var providerData = user.providerData;
                var struid = user.uid;


                var vstrChoice = 5;
                var vstrContactID = document.getElementById('strContactID').value;
                var vstrMessage = document.getElementById('strMessage').value;
                var vstrCell = document.getElementById('strCell').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrMessage=' + vstrMessage +
                    '&vstrContactID=' + vstrContactID + '&vstrCell=' + vstrCell +
                '&vstrUserID=' + struid + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/admin/contacts/" + vstrCell,
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#SMSMessageINfDIV').html(html)
                    }
                });

            })
        }
    })
});