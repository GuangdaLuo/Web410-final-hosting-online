$(document).ready(function(){
    console.log("create_check_login");
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    if($NameWithID==null){
        console.log("not log in");
        $('#body_head').html("<p align='center' style='font-size: 30px;'>You need login first to create activities.</p>s");
    }else{

        var $sp = $NameWithID.split(";");
        var $userid = $sp[1];
        var $transid = $cookie1[$NameWithID];
        $('#user_id').val($userid);
        $('#trans_id').val($transid);

        console.log("logged in "+$userid+" "+$transid);
    }
});