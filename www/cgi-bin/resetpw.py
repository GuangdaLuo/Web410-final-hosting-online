#!C:\Python27\python.exe




import cgitb
import cgi
import sqlite3
import hashlib
import json
import string
import datetime

def resetpw(username,input_code, newpw):
	conn = sqlite3.connect('hangout.db')
	cursor = conn.cursor()
	results = cursor.execute("SELECT create_time,security_code FROM sec_code,user where sec_code.username = user.username and sec_code.username = '%s';" % (username)).fetchone()
	if results is None:
		conn.close()
		return -1
	code = results[1]
	if input_code != code:
		conn.close()
		return "wrong_code"
	else:
		#print "newpw: ",newpw
		date = results[0]
		hasher = hashlib.md5()
    	hasher.update(newpw)
    	hasher.update(date)
    	encrypted = hasher.hexdigest()
    	#print "encrypted: ",encrypted
    	cursor.execute("UPDATE user SET password = '%s' WHERE username = '%s';" %(encrypted,username))
    	conn.commit()
    	conn.close()
    	return "Succeed"

cgitb.enable()

print "Content-type: application/json"
print 

user_info = cgi.FieldStorage()

username = user_info['username'].value
input_code = user_info['code'].value
newpw = user_info['newpw'].value

response = {}

# username = "testemail"
# input_code = "RDn9pj"
# newpw = "123"


res = resetpw(username,input_code,newpw)

if res == -1:
    response['response'] = -1
else:
    response['response'] = res
    
print json.dumps(response)


