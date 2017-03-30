/**
 * Created by ccatman on 12/3/2016.
 */
$(document).ready(function() {
    console.log("check_login!");
    var $cookie1 = $.cookie();
    console.log($cookie1);
    var $NameWithID = Object.keys($cookie1)[0];
    $act_id = $(location).attr('href').split('=')[1];
    if($NameWithID==null||$act_id==null) {
        $('#body_head').html("<p align='center' style='font-size: 30px;'>You have no right.</p>");
        return;
    }
    var $sp = $NameWithID.split(";");
    var $username = $sp[0];
    $("#act_id").val($act_id);

    $.ajax({
        url: '../../cgi-bin/modify_read.py',

        data: {
            username: $username,
            act_id:$act_id
        },
        async: false,
        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("login successfully");
            console.log(response);

            if (response.response == -1) {
               $('#body_head').html("<p align='center' style='font-size: 30px;'>You have no right.</p>");
            }else{
                console.log("title"+response.activity['title']);
                console.log(response.activity);
                $("#editor_title").val(response.activity[0].title);
                $("#noise").val(response.activity[0].content);
            }

        },
        error: function(request) {
            // do something
               $('#body_head').html("<p align='center' style='font-size: 30px;'>Something wrong from server</p>s");
        }
    });
});

function check_modify() {
    if(check_title()&&check_area()&&check_cate()&&check_content())
        return true;
    alert("You need to give us title,area,category and content. : )");
    return false;
}
function check_title() {

    if($('#editor_title').val().trim()!=null){

         return true;
	}
	return false;
}
function check_area() {
    var area = $('#area').val();
    if(area != -1){
        console.log("area true")
         return true;
	}
	return false;
}

function check_content() {
   var content = $('#noise').val();
   if(content.trim()!=null){
       console.log("content true")
       return true;
   }
   return false;
}