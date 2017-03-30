#!C:\Python27\python.exe


import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string
import datetime

# cgitb.enable()

# user_form = cgi.FieldStorage()

# register_str = ""
# register_str += '''<html>
#   <head>
#     <title>Welcome aboard</title>

#     <style type="text/css">
#       h1 {
#           font-size: 30px;
#           font-family: monospace;
#       }


#     </style>

#   </head>
#   <body>
# '''


def insert_user(username, password, email):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    date = str(datetime.datetime.now())
    cursor.execute("SELECT * FROM user where username = '%s'" % (username))
    if cursor.fetchone() is not None:
        return -1
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()

    cursor.execute("INSERT INTO user(username, password, email, create_time)"
                   "VALUES('%s','%s','%s','%s');" % (username, encrypted, email, date))
    conn.commit()
    conn.close()
    return 0

def get_userid_using_username(username):
    con = sqlite3.connect('hangout.db')
    cur = con.cursor()
    re = cur.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    con.close()
    if re == None: return ""
    return re[0]

def user_login(username, password):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    if results is None:
        conn.close()
        return -1
    date = None
    password_f = results[2]
    date = results[4]

    
    hasher = hashlib.md5()
    hasher.update(password)
    hasher.update(date)
    encrypted = hasher.hexdigest()
    if encrypted != password_f:
        conn.close()
        return -1

    transID = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
    cursor.execute("UPDATE user SET transID = '%s' WHERE username = '%s';" % (transID, username))
    # results2 = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    # print results2
    conn.commit()
    conn.close()
    return transID



cgitb.enable()

print "Content-type: application/json"
print

# username = "qwerww"
# password = "123"
# email = "123@qq.com"

user_info = cgi.FieldStorage()
username = user_info['username'].value
password = user_info['password'].value
email = user_info['email'].value

response = {}

if insert_user(username, password, email) == -1:
    response['response'] = -1
    # register_str += '<h1>The username already exists'
    # register_str += '''<form action="../www/index.html">
    #            <input type="submit" value="Back to Home Page">
    #          </form>'''
else:
    response['response'] = 0
    userid = get_userid_using_username(username)
    transid = user_login(username, password)
    response['userid'] = userid
    response['transid'] = transid
    

print json.dumps(response)
#     register_str += '<h1>You have create your account'
#     register_str += '<h2>Account username:' + username
#     register_str += '''<form action="/index.html">
#                <input type="submit" value="Back to Home Page">
#              </form>'''

# register_str += '''
#   </body>
# </html>

# '''





