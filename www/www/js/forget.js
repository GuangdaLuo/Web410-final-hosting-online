/**
 * forget with ajax
 * */

$(document).ready(function() {
    console.log("forget");
    $('#send_email').click(send_email);
    $('#Confirm').click(reset_pw);
});

/* send_email function */
var send_email = function() {
    console.log("send_email!");
    var $username = $('#username').val();

    if ($username != undefined) {
         console.log("user name: " + $username);
    }

    $.ajax({
        url: '../../cgi-bin/findpw.py',

        data: {
            username: $username
        },

        type: "POST",

        dataType: "json",

        success: function(response){
            console.log("success!");
            //$('#error').empty();
            if (response.response == -1) {
                $('#send_response').html("<font color=\"red\">failed to send the email, try again!</font>")
            }
            else {
                
                $('#send_response').html("<font color=\"green\">succeed to send the email, please input the security code in your email and your new password!</font>")
            }
        },

        error: function(request){
            // do something
            //console.log
            console.log("error!");
        }

    })  
    
};

/*reset_pw function*/
var reset_pw = function(){
    console.log("reset password");
    var $username = $('#username').val();
    var $code = $('#Security_code').val();
    var $newpw = $('#new_password').val();

    if ($username != undefined) {
         console.log("user name: " + $username);
    }
    if ($newpw != undefined) {
        console.log("new password: " + $newpw);
    }

    $.ajax({
        url: '../../cgi-bin/resetpw.py',

        data: {
            username: $username,
            code: $code,
            newpw: $newpw
        },

        type: "POST",

        dataType: "json",

        success: function(response){
            console.log("success!");
            console.log(response.response)
            //$('#error').empty();
            if (response.response == -1) {
                $('#reset_response').html("<font color='red'>Security code insert error, please send email agian!</font>")
            }
            else if(response.response == "wrong_code"){
                
                $('#reset_response').html("<font color='red'>Wrong code, please insert again</font>")
            }
            else{
                $('#reset_response').html("<font color='green'>Your password is changed!</font>")
            }
        },

        error: function(request){
            // do something
            //console.log
            console.log("error!");
        }

    })
};