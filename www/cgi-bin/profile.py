#!C:\Python27\python.exe





import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

print "Content-type: application/json"
print


def profile(username):
    conn1 = sqlite3.connect('hangout.db')
    cursor1 = conn1.cursor()
    results1 = cursor1.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    conn1.close()
    if results1 is None:
        return -1
    else:
        return [results1[0], results1[3]]  # user_id , email


# def profile_activity(user_id):
#     conn2 = sqlite3.connect('hangout.db')
#     cursor2 = conn2.cursor()
#     results2 = cursor2.execute("SELECT * FROM activity where user_id = '%s';" % (user_id)).fetchall()
#     conn2.close()
#     # results2 == [(1, 1, u'first activity ever', u'hello from hangout1', u'2016-11-28 19:57:42.426000', u'sport', u'Rochester', 1), (2, 1, u'second activity ever', u'hello again from hangout1', u'2016-11-28 19:57:42.426000', u'travel', u'Rochester', 0), (3, 1, u'third activity ever', u'hello one more time from hangout1', u'2016-11-28 19:57:42.426000', u'game', u'Rochester', 0)]
#     if results2 is None:
#         return -1
#     else:
#         # print results2
#         # print
#         all_activity = ""
#         for row in results2:
#             content1 = row[3].replace("<p>", "")
#             content2 = content1.replace("</p>", "")
#             all_activity += (
#             "<font color=\"green\">" + "<pre>Title:\t\t" + row[2] + "<br>Content:\t" + content2 + "<br>Create time:\t" +
#             row[4][:-7] + "<br>Catagory:\t" + row[5] + "<br>Area:\t\t" + row[6] + '<br>' + "</font>")
#         # print all_activity
#         return all_activity


def get_all_activities(user_id):
    activities_json = []
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    activities = cursor.execute("SELECT activity.act_id, title, content, category, area, reply_times, activity.create_time FROM activity, user "
                                "where activity.user_id = user.user_id AND activity.user_id = '%s'" % (user_id));
    if activities is None:
        conn.close()
        return -1

    for activity in activities:
        activity_json = { }
        # print activity
        activity_json["act_id"] = str(activity[0])
        activity_json["title"] = str(activity[1])
        activity_json["content"] = str(activity[2])
        activity_json["category"] = str(activity[3])
        activity_json["area"] = str(activity[4])
        activity_json["reply_times"] = str(activity[5])
        activity_json["create_time"] = str(activity[6])[0:-7]
        # print activity_json
        activities_json += [activity_json]

    conn.close()
    return activities_json


def get_act_title_using_id(act_id):
    con = sqlite3.connect('hangout.db')
    cur = con.cursor()
    re = cur.execute("SELECT * FROM activity where act_id = '%s';" % (act_id)).fetchone()
    con.close()
    if re == None: return ""
    return re[2]


# get_act_title_using_id(2)

def get_replier_using_id(replier_id):
    user_id = replier_id
    con = sqlite3.connect('hangout.db')
    cur = con.cursor()
    re = cur.execute("SELECT * FROM user where user_id = '%s';" % (user_id)).fetchone()
    con.close()
    if re == None: return ""
    return re[1]


# get_replier_using_id(1)

# def get_userid_using_actid(act_id):
#     con = sqlite3.connect('hangout.db')
#     cur = con.cursor()
#     re = cur.execute("SELECT * FROM activity where act_id = '%s';" % (act_id)).fetchone()
#     con.close()
#     if re == None: return ""
#     return re[1]



# return other people replied contents
def profile_reply(user_id):
    conn3 = sqlite3.connect('hangout.db')
    cursor3 = conn3.cursor()
    results3 = cursor3.execute("SELECT * FROM comment where replier_id = '%s';" % (user_id)).fetchall()
    conn3.close()
    # print results3
    if results3 is None:
        return -1
    else:
        all_replies = ""
        # print results3
        for row in results3:
            all_replies += (
            "<font color=\"green\">" + "<pre>Activity:\t" + get_act_title_using_id(row[1]) + "<br>My Reply:\t" + row[
                2] + "<br>Create time:\t" + row[3][:-7] + "<br>Replier:\t" + get_replier_using_id(
                row[4]) + '<br>' + "</font>")
        # print all_replies
        return all_replies


cgitb.enable()
user_info = cgi.FieldStorage()
username = user_info['username'].value
response = {}

# comment it before frontend use
# username = "admin"

res1 = profile(username)
user_id = res1[0]
email = res1[1]
if email == None:
    email = ""
else:
    email = "<font color=\"green\">" + email + "</font>"

# activities_str = profile_activity(user_id)
activities_dict = get_all_activities(user_id)
# print activities_dict
reply_str = profile_reply(user_id)
# print reply_str

res = {}
res['email'] = email
res['activities_dict'] = activities_dict
res['reply_str'] = reply_str

if res1 == -1 and activities_dict == -1 and reply_str == -1:
    response['response'] = -1
else:
    response = res
    response['response'] = 0

print json.dumps(response)






