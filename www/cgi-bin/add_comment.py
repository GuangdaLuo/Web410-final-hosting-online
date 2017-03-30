#!C:\Python27\python.exe



import cgitb
import cgi
import sqlite3
import datetime
import json

cgitb.enable()

fields = cgi.FieldStorage()
activity_id = fields['activity_id'].value
content = fields['content'].value
replier_id = fields['replier_id'].value
replier_name = fields['replier_name'].value
create_time = str(datetime.datetime.now())

# activity_id = "1"
# content = "world"
# replier_id = "2"
# replier_name = "admin2"

# add new comment to target activity
def add_comment():
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO comment(activity_id, content, create_time, replier_id, replier_name)"
            "VALUES('%s', '%s', '%s', '%s', '%s');" %(activity_id, content, create_time, replier_id, replier_name))
    
    
    conn.commit()
    conn.close()

curr_resp_time = 0
# increase response time by 1
def update_rpl_times():
    global curr_resp_time
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()

    # update response time
    response_time = cursor.execute("select reply_times from activity where act_id = %s;" %(activity_id))
    for _response_time in response_time:
        curr_resp_time = int(_response_time[0])
    curr_resp_time += 1
    inc_sql = '''update activity set reply_times = ? where act_id = ?'''
    paras = [curr_resp_time, activity_id]
    cursor.execute(inc_sql, paras)
    # cursor.execute("update activity set reply_times = %s where activity_id = %s;" %(curr_resp_time, activity_id))
    conn.commit()
    conn.close()

add_comment()
update_rpl_times()


print "Content-type: application/json"
print

response = {}
response['update'] = create_time[0:-7]
print json.dumps(response)


