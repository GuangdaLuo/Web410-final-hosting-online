$(document).ready(function() {
    console.log("profile.js begins");
    var $cookie1 = $.cookie();
    console.log("Cookie is " + $.cookie());
    var $NameWithID = Object.keys($cookie1)[0];
    var $sp = $NameWithID.split(";");
    var $username = $sp[0]
    console.log("profile username is  " + $username);

    if ($username != undefined) {
        console.log("profile: user name: " + $username);

        $.ajax({
            url: '../../cgi-bin/profile.py',

            data: {
                username: $username
            },

            type: "POST",

            dataType: "json",

            success: function(response) {
                console.log("get profile successfully");
                console.log(response);
                
                $('#error').empty();
                if (response.response == -1) {
                    $('#profile_res1').html("Can not get username!");
                    $('#profile_res2').html("Can not get user email!");
                    $('#profile_res3').html("Can not get user activities!");
                    $('#profile_res4').html("Can not get user replies!");
                }
                else { 
                    $('#profile_res1').html("<font color=\"green\">" + $username + "</font>");
                    $('#profile_res2').html(response.email);

                    var activities = response.activities_dict;
                    var activities_str = ""
                    for (var i = 0; i < activities.length; i++) {
                        var activity = activities[i];
                        // activities_str += "<font color=\"green\">" + "<pre>Title:\t\t" + add_link(activity.act_id, activity.title) + "<br>Content:\t" + activity.content + "<br>reply times:\t" + activity.reply_times + "<br>Create time:\t" + activity.create_time + "<br>Catagory:\t" + activity.category + "<br>Area:\t\t" + activity.area + '<br>' + "</font>"
                        activities_str += "<font color=\"green\">" + "<pre>Title:\t\t" + add_link(activity.act_id, activity.title) + "<br>reply times:\t" + activity.reply_times + "<br>Create time:\t" + activity.create_time + "<br>Catagory:\t" + activity.category + "<br>Area:\t\t" + activity.area + '<br>' + "</font>"
                    }
                    $('#profile_res3').html(activities_str);
                    $('#profile_res4').html(response.reply_str);
                    console.log("multiple response" + response);
                    
                }

            },

            error: function(request) {
                console.log("profile error!");
            }
        });
    } else {
        console.log("Cannot get username!");
    }

});

function add_link(id, title) {
    return "<a href=\"../../cgi-bin/" + "view_activity.py?id=" + id + "\">" + title + "</a>";
}



    



