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
def get_all_activities():
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT activity.act_id, title, username, reply_times, activity.create_time FROM activity, user "
                                "where activity.user_id = user.user_id");
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


# def get_activities_by_catetories():
def get_by_category(category):
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT activity.act_id, title, username, reply_times, activity.create_time FROM activity, user "
                                "where activity.user_id = user.user_id and category = " + "'" + category + "'")
    if activities is None:
        conn.close()
        return -1

    for activity in activities:
        activity_json = {}
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

# get activities by keyword
def get_by_keyword(keyword):
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()

    #search_sql = '''select * from activity'''
    search_sql = '''SELECT activity.act_id, title, username, reply_times, activity.create_time 
                    FROM activity, user
                    where activity.user_id = user.user_id'''
    activities = cursor.execute(search_sql)

    if activities is None:
        conn.close()
        return -1

    for activity in activities:
        activity_json = {}

        if keyword in str(activity[1]):
            activity_json["act_id"] = str(activity[0])
            activity_json["title"] = str(activity[1])
            activity_json["username"] = str(activity[2])
            activity_json["reply_times"] = str(activity[3])
            activity_json["create_time"] = str(activity[4])[0:-7]
            activities_json += [activity_json]

    conn.close()
    return activities_json


cgitb.enable()
print "Content-type: application/json"
print

activities_json = {}
fields = cgi.FieldStorage()
# fetch_type = cgi.FieldStorage()['type'].value
fetch_type = fields['type'].value

# fetch_type = "category"

# call corresponding function by fetch type
if fetch_type == "all":
    activities_json['activity'] = get_all_activities()
elif fetch_type == "category":
    activities_json['sport'] = get_by_category("sport")
    activities_json['travel'] = get_by_category("travel")
    activities_json['game'] = get_by_category("game")
    activities_json['event'] = get_by_category("event")
elif fetch_type == "keyword":
    keyword = fields['keyword'].value
    activities_json['activity'] = get_by_keyword(keyword)

print json.dumps(activities_json)



