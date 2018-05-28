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

//CreateTicketINFDIV
var thisCreateTicketButt = document.getElementById("CreateTicketButt");
thisCreateTicketButt.addEventListener("click", function () {
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


                var vstrChoice = 3;
                var vstrNames = document.getElementById('strNames').value;
                var vstrSurname = document.getElementById('strSurname').value;
                var vstrCell = document.getElementById('strCell').value;
                var vstrEmail = document.getElementById('strEmail').value;
                var vstrSubject = document.getElementById('strSubject').value;
                var vstrBody = document.getElementById('strBody').value;

                var vstrTicketPreference = document.getElementById('strTicketPreference').value;
                var vstrDepartment = document.getElementById('strDepartment').value;
                var dataString = '&vstrChoice=' + vstrChoice + '&vstrSubject=' + vstrSubject + '&vstrBody=' + vstrBody +
                    '&vstrTicketPreference=' + vstrTicketPreference + '&vstrDepartment=' + vstrDepartment + '&vstrNames=' + vstrNames +
                    '&vstrSurname=' + vstrSurname + '&vstrCell=' + vstrCell + '&vstrEmail=' + email + '&vstrUserID=' + struid + '&vstrAccessToken=' + accessToken;
                $.ajax({
                    type: "post",
                    url: "/contact",
                    data: dataString,
                    cache: false,
                    success: function (html) {
                        $('#CreateTicketINFDIV').html(html)
                    }
                });
            })
        }
    })
});
