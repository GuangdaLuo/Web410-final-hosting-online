/**
 * Created by ccatman on 12/3/2016.
 */
$(document).ready(function() {
    console.log("check_login!");
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    if($NameWithID==null)
        return;
    var $sp = $NameWithID.split(";");
    var $username = $sp[0]
    console.log("loggin name:"+$username+"the name:"+$("#create_username").val());
    if($("#create_username").val()==$username){
        $("#modify_op").html("<button id='user_modify'>Modify</button><br/><button id='user_delete'>Delete</button>");
    }
    $("#user_modify").click(user_modify);
    $("#user_delete").click(user_delete);

});
var user_modify = function () {
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    if($NameWithID==null)
        return;
    var $act_id=$("#act_id").val();
    window.location.href = '../modify.html?act_id='+$act_id;
};
var user_delete = function () {
        var $cookie1 = $.cookie();
        console.log($cookie1);
        var $NameWithID = Object.keys($cookie1)[0];
        if ($NameWithID == null) {
            console.log("not logged in")
            return;
        }
        var $sp = $NameWithID.split(";");

        var $user_id = $sp[1]
        var $act_id = $("#act_id").val();
        console.log("$user_id:" + $user_id + ",oper:1,act_id:" + $act_id);

        $.ajax({
            url: '../../cgi-bin/user_modify.py',

            data: {
                user_id: $user_id,
                opera: 1,
                act_id: $act_id
            },
            type: "POST",

            dataType: "json",

            success: function (response) {
                console.log("return success from py");
                console.log(response);

                if (response.response == -1) {
                    console.log("delete fail")
                }
                else {
                    console.log("delete success")
                    $('#body_head').html("<p align='center' style='font-size: 30px;'>Delete the thread successfully</p>");

                }

            },

            error: function (request) {
                console.log("error");
            }
    });

};
