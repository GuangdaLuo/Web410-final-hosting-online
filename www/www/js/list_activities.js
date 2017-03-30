/*
 * This script fetches  activities from database and list 
 * them both by categories and by post data (or by popularity)
 * */

$(document).ready(function() {
    console.log("list activities");
    list_activities_by_category();
    list_all_activities();
});

var list_activities_by_category = function() {
    /* to be done*/
    console.log("list activities by categories");

    $.ajax({
        url: '../../cgi-bin/get_activities.py',

        data: {
            type: "category"
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("get_activities.py executed");

            if (response != null) {
                /* list activities by categories */
                for(var category in response) {
                    console.log(category);
                    /* handle activities by category */
                    var activities = response[category];
                    for (var i = 0; i < activities.length; i++) {
                        var activity = activities[i];
                        /* add a new <li> */
                        // var li = "<li>" + activity.title + "</li>";
                        var li = "<li>" + add_link(activity.act_id, activity.title) + "</li>";
                        $('#' + category).append(li);
                    }
                }
            }
        },

        error: function() {
            console.log("ERROR: fetching activities by categories failed");
        }
    });
};

/* list all activities by their created time */
var list_all_activities = function() {
    console.log("start to list activities");

    $.ajax({
        url: '../../cgi-bin/get_activities.py',

        data: {
            type: "all"
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
            console.log("get_activities.py executed");

            /* start to list all activities */
            if (response != null) {
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
            }

        },

        error: function(response) {
            console.log("ERROR: fetch all activities failed");
            // error
            console.log(response);
        }
    }); 
};

var add_link = function(id, title) {
    return "<a href=\"../../cgi-bin/" + "view_activity.py?id=" + id + "\">" + title + "</a>";
}
