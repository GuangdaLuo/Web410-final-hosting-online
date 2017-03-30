#!C:\Python27\python.exe





import cgitb
import cgi
import sqlite3
import hashlib
import json
import random
import string
import smtplib

from email.mime.text import MIMEText
from email.header import Header
from random import Random

def find_email(username):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where username = '%s';" % (username)).fetchone()
    if results is None:
        conn.close()
        return -1

    email = results[3]
    #print email

    conn.close()
    return email

# For backend testing only:
# user_login("asd", "asd")

def send(email):
  mail_host="smtp.gmail.com" #server
  mail_user="zsw9819"    #username
  mail_pass="zsw5732738"   #password 

  sender = 'zsw9819@gmail.com'
  receiver = email
  s = ''
  chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
  length = len(chars) - 1
  random = Random()
  for i in range(6):
      s+=chars[random.randint(0, length)]



  message = MIMEText(s, 'plain', 'utf-8')
  message['From'] = Header("Hang Out", 'utf-8')
  message['To'] =  Header(username, 'utf-8')

  subject = 'Find Your Hang Out Password'
  message['Subject'] = Header(subject, 'utf-8')

  
  try:
   smtpObj = smtplib.SMTP() 
   smtpObj.connect(mail_host, 587)    # 587 SMTP port
   smtpObj.ehlo()
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(mail_user,mail_pass)  
   smtpObj.sendmail(sender, receiver, message.as_string())

   #insert the security code into database
   conn = sqlite3.connect('hangout.db')
   cursor = conn.cursor()

   cursor.execute("DELETE FROM sec_code WHERE username = '%s'" %(username))

   cursor.execute("INSERT INTO sec_code(username, security_code)"
                  "VALUES('%s','%s');" %(username, s))

   conn.commit()
   conn.close()

   #print "succeed"
   return "Succeed"
  except smtplib.SMTPException as ins:
    print ins
    return -1

cgitb.enable()


print "Content-type: application/json"
print 

user_info = cgi.FieldStorage()

username = user_info['username'].value

#username = "testemail"

response = {}

email = find_email(username)
if email == -1:
    response['response'] = -1
else:
    res = send(email)

    if res == -1:
        response['response'] = -1
    else:
        response['response'] = res
    
print json.dumps(response)






