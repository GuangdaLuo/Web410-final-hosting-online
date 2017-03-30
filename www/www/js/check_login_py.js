$(document).ready(function() {
    console.log("check_login!");
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    if($NameWithID==null)
        return;
    var $sp = $NameWithID.split(";");
    var $username = $sp[0]
    var $userid = $sp[1]
    var $transid = $cookie1[$NameWithID];
    console.log($transid);
    console.log("new username and transid: "+ $username + "," + $userid + "," + $transid);

    if ($username != undefined) {
        console.log("user name: " + $username + $transid);


        $.ajax({
            url: '../../cgi-bin/check_login.py',

            data: {
                username: $username,
                transid: $transid
            },

            type: "POST",

            dataType: "json",

            success: function(response) {
                console.log("check_login successfully");
                console.log(response);

                $('#error').empty();
                if (response.response == -1) {

                }
                else {
                    $('.login').html("Welcome, " + $username + "&nbsp&nbsp&nbsp<a href='../profile.html'>profile</a>&nbsp&nbsp&nbsp");
                    $('.login').append("<button id='log_out' >logout</button>");
                    $('#log_out').click(log_out);

                }

            },

            error: function(request) {
                // do something
            }
        });
    } else {
        console.log("log in check failed");
        // $('.log_out').hide();
        // $('.activity').hide();
        // $('#check_login_res').html("<font color=\"red\">Please log in first</font>");
    }

});








