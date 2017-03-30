#!C:\Python27\python.exe





print 'Content-Type: text/html'
print

print '''
<!DOCTYPE html>
<html>
<head>
	<title>Hang OUT!</title>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
	<script src="../www/js/widgEditor.js"></script>
	<script src="../www/js/jquery.cookie.js"></script>
	<script type="text/javascript" src="../www/js/login.js"></script>
	<script src="../www/js/log_out_py.js"></script>
	<script src="../www/js/check_login_py.js"></script>
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
				<li><a  href="../www/index.html">Home</a></li>
				<li class="dropdown"><a class="active" href="../www/activity.html">Activites</a>
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
			<p align='center' style='font-size: 30px;'>
	'''
import sqlite3
import cgi
import cgitb; cgitb.enable()

def get_category_name(category):
    if(category=="1"):
        return "sport"
    if(category=="2"):
        return "travel"
    if(category=="3"):
        return "game"
    if(category=="4"):
        return "event"

def modify_activity(form):
    user_id=form['user_id'].value
    act_id=form['act_id'].value
    content=form['noise'].value
    category = form['category'].value
    category = get_category_name(category)
    area = form['area'].value
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activity where "
                   "user_id = '%s' and act_id= '%s'" % (user_id, act_id))
    result= cursor.fetchone()
    if result is None:
        return -1

    cursor.execute("UPDATE activity SET content = '%s',area = '%s',category='%s'"
                   " where act_id = '%s'"% (content, area, category, act_id))
    conn.commit()
    conn.close()
    return 0

create_form = cgi.FieldStorage()
result = modify_activity(create_form)
if result == -1:
    print 'No modify right'
else:
    print 'Modify Successfully'
print '''
			</p>
		</div>

	</div>


</body>
</html>

print '''