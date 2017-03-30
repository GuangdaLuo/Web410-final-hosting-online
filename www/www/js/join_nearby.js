/*
 * This script fetches  activities from database and list
 * them both by categories and by post data (or by popularity)
 * */

$(document).ready(function() {
    console.log("list activities");
    $("#area").change(join);
});


/* list all activities by their created time */
var join = function list_all_activities() {
    console.log("start to list activities");

    if($("#area").val()==-1)
        return;
    console.log("area:"+$("#area").val());
    $.ajax({
        url: '../../cgi-bin/join_near.py',

        data: {
            area: $("#area").val()
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("get_activities.py executed");

            /* start to list all activities */
            if (response != null){
                console.log(response);

                $(".table_entry").remove();

                var activities = response.activity;
                var $all_activities = $('#all_activities');
                for (var i = 0; i < activities.length; i++) {
                    var activity = activities[i];
                    /* add a new table row in this table */
                    var tr = "<tr class=\"table_entry\">";
                    tr += "<td>" + add_link(activity.act_id, activity.title) + "</td>";
                    tr += "<td>" + activity.username + "</td>";
                    tr += "<td>" + activity.reply_times + "</td>";
                    tr += "<td>" + activity.create_time + "</td>";
                    tr += "</tr>";
                    $all_activities.append(tr);
                }
            }else{
                console.log("null");
                $('#all_activities').html();
            }

        },

        error: function(response) {
            console.log("ERROR: fetch all activities failed");
            // error
            console.log(response);
        }
    });
};

function add_link(id, title) {
    return "<a href=\"../../cgi-bin/" + "view_activity.py?id=" + id + "\">" + title + "</a>";
}
