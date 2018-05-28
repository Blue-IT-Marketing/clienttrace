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


                var vstrChoice = 0;
                var vstrComment = document.getElementById("strComment").value;
                var vstrTicketID = document.getElementById("strTicketID").value;
                var vstrThreadID = document.getElementById("strThreadID").value;
                var vstrUserID = document.getElementById("strUserID").value;
                var dataString = "&vstrChoice=" + vstrChoice + '&vstrComment=' + vstrComment + '&vstrTicketID=' + vstrTicketID +
                    '&vstrThreadID=' + vstrThreadID + '&vstrUserID=' + vstrUserID + '$vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact/tickets/" + vstrTicketID,
                    data: dataString,
                    cache: false,
                    success: function (data) {
                        $('#TicketSystemINFDIV').html(data);
                        document.getElementById("strComment").value = "";
                    }
                });
            })
        }
    })
});
function UpdateChat() {
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


                var vstrChoice = 1;
                var vstrTicketID = document.getElementById("strTicketID").value;
                var vstrThreadID = document.getElementById("strThreadID").value;
                var vstrUserID = document.getElementById("strUserID").value;

                var dataString = "&vstrChoice=" + vstrChoice + '&vstrTicketID=' + vstrTicketID +
                    '&vstrThreadID=' + vstrThreadID + '&vstrUserID=' + vstrUserID + '&vstrEmail=' + email + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact/tickets/" + vstrTicketID,
                    data: dataString,
                    cache: false,
                    success: function (data) {
                        $('#TicketSystemINFDIV').html(data)
                    }
                });
            })
        }
    })
}
// TODO- Note it might be easier to just implement push notifications as this methods uses up resources
setInterval(UpdateChat,5000);