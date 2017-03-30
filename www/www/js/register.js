$(document).ready(function() {
    console.log("start to register");
    $('#register').click(register);
});

var register = function() {
    var $username = $('#username').val();
    var $password = $('#password').val();
    var $email = $('#email').val();

    var pattern="^[_/.a-z0-9]+@[a-z0-9]+[/.][a-z0-9]{2,}$";
    var check=new RegExp(pattern);
	if(!check.test($email)) {
        return false;
    }

    console.log("register get: " + $username + " " + $password + " " + $email);

    $.ajax({
        url: '../../cgi-bin/register.py',

        data: {
            username: $username,
            password: $password,
            email: $email
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("register successfully");
            console.log(response);
            
            $('#error').empty();
            if (response.response == -1) {
                console.log("register.py returns -1");
            }
            else {
                var $cookie_old = $.cookie();
                console.log("Old cookie: " + $cookie_old)
                var $NameWithID_old = Object.keys($cookie_old)[0];
                console.log("Old NameWithID_old: " + $NameWithID_old)
                if ($NameWithID_old != null) {
                    $.removeCookie($NameWithID_old);
                    console.log("Old NameWithID_old removed: " + $NameWithID_old)
                }

                console.log("Welcome, " + $username + " , register succeed!");
                $('#register_res').html("<font color=\"blue\" size=\"5\">Register succeed!  Welcome to HangOut! </font>")
                // $('.login').append("<button id='log_out' >logout</button>");
                $('.register').hide();
                var $NameWithID = $username + ";" + response.userid;
                $.cookie($NameWithID, response.transid, { expires: 60 });
                // Set a cookie at Client with the returned transID (transaction ID) expires within 60 days

                // var $NameWithID = $username + ";" + response.userid;
                // $.cookie($NameWithID, response.transid, { expires: 60 });
                
            }

        },

        error: function(request) {
            console.log("register.js error");
        }
    });
    
};

