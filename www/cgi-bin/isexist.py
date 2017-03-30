#!C:\Python27\python.exe







import cgitb
import cgi
import sqlite3
import json

print "Content-type: application/json"
print


def register_check(username):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    conn.close()
    if results is None:
        return 0
    else:
        return -1


cgitb.enable()

user_info = cgi.FieldStorage()

username = user_info['username'].value

response = {}

res = register_check(username)
if res == -1:

    response['response'] = -1
else:
    response['response'] = 0

print json.dumps(response)






