/**
 * login with ajax
 * */

$(document).ready(function() {
    console.log("start to log in");
    $('#login').click(login);
});
/* clear username and password field */
function clear_login_info() {
    console.log("clear user name and password");
    $('#username').val('');
    $('#password').val('');
}


/* login function */
var login = function() {
    var $username = $('#username').val();
    var $password = $('#password').val();
    console.log("user name: " + $username);

    $.ajax({
        url: '../../cgi-bin/login.py',

        data: {
            username: $username,
            password: $password
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("login successfully");
            console.log(response);
            
            $('#error').empty();
            if (response.response == -1) {
                $('#login_td_span').html('<font color=\"red\">wrong username or password</font>');
                clear_login_info();
                
            }
            else {
                $('.login').html("Welcome, " + $username + "&nbsp&nbsp&nbsp<a href='./profile.html'>profile</a>&nbsp&nbsp&nbsp")
                $('.login').append("<button id='log_out' >logout</button>");
                $('#log_out').click(log_out);
                // Set a cookie at Client with the returned transID (transaction ID) expires within 60 days

                var $NameWithID = $username + ";" + response.userid;
                $.cookie($NameWithID, response.transid, { expires: 60 });
                
            }

        },

        error: function(request) {
            // do something
        }
    });
    
};

