#!C:\Python27\python.exe


import cgitb
import cgi
import sqlite3
import json


def delete_activity(user_id,act_id):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM activity where user_id = '%s' and act_id = '%s' " % (user_id, act_id))
    cursor.execute("DELETE FROM image where activity_id = '%s'" % (act_id))
    cursor.execute("DELETE FROM comment where activity_id = '%s'" % (act_id))
    conn.commit()
    conn.close()


# For backend testing only:
# user_login("asd", "asd")

cgitb.enable()
print "Content-type: application/json"
print

activities_json = {}
form = cgi.FieldStorage()
user_id = form['user_id'].value
act_id = form['act_id'].value
opera = form['opera'].value
# user_id=2
# act_id=5
# opera=1
# if opera == 1:#delete operation
delete_activity(user_id, act_id)
activities_json['response'] = 1

# call corresponding function by fetch type

print json.dumps(activities_json)





