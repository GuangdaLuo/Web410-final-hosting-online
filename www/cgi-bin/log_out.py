#!C:\Python27\python.exe








import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string

def user_logout(username):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    transID = "-1"
    cursor.execute("UPDATE user SET transID = '%s' WHERE username = '%s';" % (transID, username))
    # results2 = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    # print results2
    conn.commit()
    conn.close()
    return 0


cgitb.enable()


print "Content-type: application/json"
print 

user_info = cgi.FieldStorage()

username = user_info['username'].value

response = {}

res = user_logout(username)
if res == -1:
    # print '<h1>Wrong username or password'
    response['response'] = -1
else:
    response['response'] = 0
    
print json.dumps(response)






