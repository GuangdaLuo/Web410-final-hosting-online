$(document).ready(function() {
    console.log("log out!");

    $('#log_out').click(log_out);
});

/* login function */
var log_out = function() {
    var $cookie1 = $.cookie();
    console.log("logout: " + $cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    var $sp = $NameWithID.split(";");
    var $username = $sp[0]
    var $userid = $sp[1]
    console.log("logout: " + $sp[0] + "  " + $sp[1]);
    // var res = str.split(" ");
    console.log("user name: " + $username);

    $.ajax({
        url: '../../cgi-bin/log_out.py',

        data: {
            username: $username,
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("log_out successfully");
            console.log(response);
            
            $('#error').empty();
            if (response.response == -1) {
                $('#log_out_res').html("<font color=\"red\">Sorry, log out failed!</font>");
            }
            else {
                $.removeCookie($NameWithID);
                window.location.href = './index.html';
            }

        },

        error: function(request) {
            // do something
        }
    });
    
};


