$(document).ready(function() {
    
    $('#submit').click(add_comment);
});

var add_comment=function(){
    console.log("add some comment check if logged in");
    // var $cookie = $.cookie();

    var $cookie1 = $.cookie();
    var $NameWithID = Object.keys($cookie1)[0];
    if($NameWithID==null){
        console.log("not log in");
        alert("You need login first");
        return;
    }else{
        console.log("logged in");
        var $sp = $NameWithID.split(";");
        var $userid = $sp[1];
        var $transid = $cookie1[$NameWithID];
        $('#user_id').val($userid);
        $('#trans_id').val($transid);

        console.log("logged in "+$userid+" "+$transid);
    }

    var $activity_id = $(location).attr('href').split('?')[1].substring(3);
    console.log($activity_id);
    var $content = $('#reply_area').val();
    console.log($content);
    var $replier_name = Object.keys($.cookie())[0].split(';')[0];
    var $replier_id = Object.keys($.cookie())[0].split(';')[1];
    console.log($replier_name);
    
    $.ajax({
        url: '../../cgi-bin/add_comment.py',

        data: {
            replier_id: $replier_id,
            replier_name: $replier_name,
            content: $content,
            activity_id: $activity_id
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("add comment successfully");
            console.log(response);
            // add this new comment to the end of comment area
            $table=$("#view_table tbody");
            var new_comment = "<tr><td class='view_col1'>";
            new_comment+="<p>username: " + $replier_name + "</p>";
            new_comment+="<p>time: " + response.update + "</p></td><td  class='view_col2'>";
            new_comment+="<p>" + $content + "</p></td><td class='view_col3'></td>";

            $table.append(new_comment);

            // new_comment += "<div class=\"left_comment\">";
            // new_comment += "<p>username: " + $replier_name + "</p>";
            // new_comment += "<p>time: " + response.update + "</p></div>";
            // new_comment += "<div class=\"right_comment\">";
            // new_comment += "<p>" +  + "</p></div></div>";
            // $('#content_comment').append(new_comment);
            $('#reply_area').val('');

            console.log("end of add a new comment");
        },

        error: function(response) {
            console.log("failed to add comment");
            console.log(response);
        }
    });
};
