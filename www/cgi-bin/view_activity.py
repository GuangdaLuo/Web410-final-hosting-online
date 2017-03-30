#!C:\Python27\python.exe






import cgi
import cgitb
import sqlite3

cgitb.enable()

# fetch the activity id
act_id = cgi.FieldStorage()['id'].value

activity = {}
comments = []

def get_activity():
    global activity
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    _activity = cursor.execute("SELECT * FROM activity WHERE act_id = " + act_id)

    if _activity is None:
        conn.close()
        return
    for __activity in _activity:
        activity['act_id'] = str(__activity[0])
        activity['user_id'] = str(__activity[1])
        activity['title'] = str(__activity[2])
        activity['content'] = str(__activity[3])
        activity['create_time'] = str(__activity[4])[0 : -7]
        activity['category'] = str(__activity[5])
        activity['area'] = str(__activity[6])
        activity['reply_times'] = str(__activity[7])
        username = cursor.execute("SELECT username FROM user where user_id = " + activity['user_id'])
        for name in username:
        	activity['username'] = str(name[0])
        img_path = cursor.execute("select path from image where activity_id = " + act_id)
        for _img_path in img_path:
            activity['img_path'] = "../www/pics/memberphotos/" + str(_img_path[0])

    conn.close()


def get_comments():
    global comments
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    _comments = cursor.execute("select * from comment where activity_id = " + act_id)

    if _comments is None:
        conn.close()
        return

    for _comment in _comments:
        comment = { }
        comment['com_id'] = str(_comment[0])
        comment['activity_id'] = str(_comment[1])
        comment['content'] = str(_comment[2])
        comment['create_time'] = str(_comment[3])[0 : -7]
        comment['replier_id'] = str(_comment[4])
        comment['replier_name'] = str(_comment[5])
        comments += [comment]
    conn.close()

get_activity()
get_comments()

print "Content type: text/html"
print

print '''
<!DOCTYPE html>
<html>
<head>
	<title>Hang OUT!</title>
	
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="../www/js/widgEditor.js"></script>
	<script src="../www/js/jquery.cookie.js"></script>
	<script src="../www/js/login.js"></script>
	<script src="../www/js/log_out_py.js"></script>
	<script src="../www/js/check_login_py.js"></script>
	<script src="../www/js/add_comment.js"></script>
	<script src="../www/js/modify_check.js"></script>
	<script src="../www/js/search.js"></script>
	<style type="text/css" media="all">
		@import "../www/css/main.css";
		@import "../www/css/widgEditor.css";
	</style>
	<link rel="stylesheet" type="text/css" href="../www/css/style.css">
	<link rel="stylesheet" type="text/css" href="../www/css/slide.css">
	
</head>

<body>
	<div id="header">
		<div id="top_area">
			<div id="logo_bar">Hang OUT</div>
			<div id="login_bar">


				<div class="login">
					<table>
						<tr>
							<td>username:</td>
							<td><input type="text" id="username"></td>
							<td><a href="../www/register.html">Sign up</a></td>
						</tr>
						<tr>
							<td>password:</td>
							<td><input type="password" id="password"></td>
							<td><a href="../www/forget.html">forget?</a></td>

						</tr>
						<tr>
							<td></td>
							<td colspan="2" id="login_td"><button type="button" id="login">login</button><span id="login_td_span"></span>	</td>
						</tr>
					</table>
				</div>

			</div>
		</div>
		<div id="menu">

			<ul>
				<li><a href="../www/index.html">Home</a></li>
				<li class="dropdown"><a href="../www/activity.html">Activites</a>
				<div class="dropdown-content">
					<a href="#">Sports</a>
					<a href="#">Games</a>
					<a href="#">Events</a>
					<a href="#">Travel</a>
				</div>
				</li>

				<li><a href="../www/join_nearby.html">Join Nearby</a></li>
				<li><a href="../www/new_activity.html">Create New</a></li>


				<div id="search_bar">
					<input type="text" name="search_bar" id= "search"/>
					<button id="search_btn">GO!</button>
				</div>
			</ul>

	
			
		</div>
	</div>
	<div id="body_main">
		<div id="body_head">
		<div id="view_table">
		<table id="view_table">
		    <tr><td colspan='3' class="table_title">
'''

print activity['title'] + "</td>"

# print the content of the activity
print "<tr>"
print "<td class='view_col1'>"
print "<p >username: " + activity['username'] + "</p>"
print "<p>time: " + activity['create_time'] + "</p>"
print "<input type='text' id='act_id' value='"+activity['act_id']+"' hidden>"
print "<input type='text'id='create_username' value='"+activity['username']+"' hidden>"

print "</td><td class='view_col2'>"
if 'img_path' in activity:
    print "<img style=\"height:200px; width:auto\" src=\"" + activity['img_path'] + "\">"
print "<p>" + activity['content'] + "</p>"

print "</td>" \
      "<td class='view_col3' id='modify_op'></td>"


# print comments
for comment in comments:
    print "<tr>"
    print "<td class='view_col1'>"
    print "<p>username: " + comment['replier_name'] + "</p>"
    print "<p>time: " + comment['create_time'] + "</p>"
    print "</td><td class='view_col2'>"
    print "<p>" + comment['content'] + "</p>"
    print "</td>" \
          "<td class='view_col3'></td>"

print "</table></div>"

# add editor
print '''
		<div id="re_editor">
				<textarea id="reply_area" name="reply"></textarea>
				<button id="submit">reply</button>
		</div></div></div>
		'''
print "</body></html>"


