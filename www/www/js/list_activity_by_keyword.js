$(document).ready(function() {
    console.log("list activities by keyword");
    list_activities_by_keyword();
});


/* list activities by keyword */
var list_activities_by_keyword = function() {
	console.log("list activities by keyword");
	$keyword = $(location).attr('href').split('=')[1];
	//console.log("keyword = " + $keyword);

    $.ajax({
        url: '../../cgi-bin/get_activities.py',

        data: {
            type: "keyword",
            //what: "first"
            keyword: $keyword
        },

        type: "POST",

        dataType: "json",

        success: function(response) {
        	console.log("get activities by keyword");

        	if (response != null) {
                var activities = response.activity;
                var $interested_activities = $('#interested_activities');
                for (var i = 0; i < activities.length; i++) {
                    var activity = activities[i];
                    /* add a new table row in this table */
                    var tr = "<tr class=\"table_entry\">";
                    tr += "<td>" + add_link(activity.act_id, activity.title) + "</td>";
                    tr += "<td>" + activity.username + "</td>";
                    tr += "<td>" + activity.reply_times + "</td>";
                    tr += "<td>" + activity.create_time + "</td>";
                    tr += "</tr>";
                    $interested_activities.append(tr);
                }
            }
         },

         error: function(response) {
         	console.log("fetch activity by keyword failed");
         	console.log(response);
         }
     });
};

var add_link = function(id, title) {
    return "<a href=\"../../cgi-bin/" + "view_activity.py?id=" + id + "\">" + title + "</a>";
}