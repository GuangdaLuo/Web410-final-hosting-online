#!C:\Python27\python.exe




'''
get_all_activities fetch required information about activities;
possible ways to fetch:
    1. all
    2. by categories
    3. by creator
    4. search by keyword
'''

import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string


# get all activities from activity table
def check_user_activity(username, act_id):
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT title,content FROM activity, user "
                                "where activity.user_id = user.user_id and act_id = '%s' and username='%s'" % (act_id, username)).fetchone();
    if activities is None:
        conn.close()
        return -1


    activity_json = {}
    # print activity
    activity_json["title"] = str(activities[0])
    activity_json["content"] = str(activities[1])
    # print activity_json
    activities_json += [activity_json]

    conn.close()
    return activities_json



cgitb.enable()
print "Content-type: application/json"
print

activities_json = {}
fields = cgi.FieldStorage()
# fetch_type = cgi.FieldStorage()['type'].value
username = fields['username'].value
act_id = fields['act_id'].value
result=(check_user_activity(username, act_id))
if result == -1:
    activities_json['response']=-1
else:
    activities_json['response'] =1
    activities_json['activity'] = result
# fetch_type = "category"

# call corresponding function by fetch type


print json.dumps(activities_json)



