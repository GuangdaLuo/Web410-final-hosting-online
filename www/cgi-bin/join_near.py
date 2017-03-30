#!C:\Python27\python.exe







import cgitb
import cgi
import sqlite3
import json


def get_activity_by_area(area):
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT act_id, title, username, reply_times, activity.create_time FROM activity, user "
                                "where activity.user_id=user.user_id and area = '%s'" % area)
    if activities is None:
        conn.close()
        return -1

    for activity in activities:
        activity_json = { }
        # print activity
        activity_json["act_id"] = str(activity[0])
        activity_json["title"] = str(activity[1])
        activity_json["username"] = str(activity[2])
        activity_json["reply_times"] = str(activity[3])
        activity_json["create_time"] = str(activity[4])[0:-7]
        # print activity_json
        activities_json += [activity_json]

    conn.close()
    return activities_json


# For backend testing only:
# user_login("asd", "asd")

cgitb.enable()
print "Content-type: application/json"
print

activities_json = {}
area = cgi.FieldStorage()['area'].value
# fetch_type = "category"

# call corresponding function by fetch type
activities_json['activity'] = get_activity_by_area(area)


print json.dumps(activities_json)





