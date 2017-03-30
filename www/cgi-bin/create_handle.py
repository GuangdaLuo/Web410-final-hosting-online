#!C:\Python27\python.exe







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
'''

try:
  import msvcrt,os
  msvcrt.setmode( 0, os.O_BINARY ) # stdin  = 0
  msvcrt.setmode( 1, os.O_BINARY ) # stdout = 1
except ImportError:
  pass


import sys, os, traceback, re
import random
import cgi
import cgitb; cgitb.enable()
import sqlite3
import datetime


def strip_path( fpname ):
  """strip off leading path and drive stuff from dos/unix/mac file full name
  takes care of '/' ':' '\' '%2f' '%5c' '%3a'
  """
  fname = re.sub( r"(%(2f|2F|5c|5C|3a|3A))|/|\\|:", '/', fpname )
  delim = fname.rfind( '/' ) # -1 for not found, will return full fname
  return fname[delim+1:]


def check_ext( file_name, ext_set ):
  ext = file_name.rfind('.')
  if ext < 0:
    return False
  ext = file_name[ext+1:].lower()
  # was re.match( '^(gif)|(jpg)|(zip)$', ext, re.I )
  exts = ext_set.lower().split(',')
  for good_ext in exts:
    if ext == good_ext:
      return True
  return False


class UploadException:
  def __init__(self,rsn): self.reason = rsn

NO_FILE_FIELD = -1
NO_FILENAME   = -2
BAD_EXTENTION = -3
NO_FILE       = -4



def process_fileitem( file_item_name, form, local_file_path , allowed_file_types):
  """Gets file from form field file_item_name and saves it with the original
  file name to local_file_path. Returns (file_length,file_name) if success.
  Otherwise raise UploadException( NO_FILE_FIELD|NO_FILENAME|BAD_EXTENTION|NO_FILE )
  """

  if not form.has_key( file_item_name ):
      return -1

  file_item = form[ file_item_name ]

  if not file_item.filename:
    return -1
  remote_file_name = file_item.filename
  file_name = strip_path( remote_file_name )

  if not check_ext( file_name, allowed_file_types ):
    raise UploadException( BAD_EXTENTION )

  short_id = str(random.randint(1, 999999999))
  extension = os.path.splitext(file_name)[1]
  new_file_name = short_id+extension
  #if the file name exits regenerate one
  while(os.path.isfile(local_file_path+new_file_name)):
      short_id = str(random.randint(1, 999999999))
      new_file_name = short_id + extension

  local_file_name = os.path.join( local_file_path, new_file_name )
  if not file_item.file:
    raise UploadException( NO_FILE )

  data = file_item.file.read( 5*1024*1024 ) # max 5 megabyte
  # or data = fileitem.value
  # or data = form.getvalue( file_item_name, "" )
  fstrm = open( local_file_name, "wb" )
  fstrm.write( data )
  fstrm.close()
  return  new_file_name


def get_category_name(category):
    if(category=="1"):
        return "sport"
    if(category=="2"):
        return "travel"
    if(category=="3"):
        return "game"
    if(category=="4"):
        return "event"

def create_login_check(userid, transid):
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * FROM user where user_id = '%s';" % (userid)).fetchone()
    conn.close()
    if results is None:
        return -1
    elif results[5] == transid:
        return 0
    else:
        return -1

def insert_activity(form):
    title=form['title'].value
    noise = form['noise'].value
    category = form['category'].value
    area = form['area'].value
    user_id=form['user_id'].value
    trans_id=form['trans_id'].value
    if(create_login_check(user_id,trans_id)!=0):
        print '''
           <div style="margin-left:20%;margin-top:50px; font-size:25px; font-family:fantasy;">Do not try to mess up my web pages</div>
        '''
        return 0
    file_field_name = "picture"
    loc_path = "../www/pics/memberphotos"
    file_types = "jpg,png,gif"
    conn = sqlite3.connect('hangout.db')
    cursor = conn.cursor()
    date = str(datetime.datetime.now())
    cursor.execute("SELECT * FROM activity where act_id = (select MAX(act_id) from activity)")
    results=cursor.fetchone()
    if results is None:
        new_id = 0
    else:
        new_id=int(results[0])+1

    try:
        filename=process_fileitem(file_field_name, form, loc_path, file_types)
    except:
        print ''' Something Wrong with upload'''
        return 0
    if(filename != -1):
        cursor.execute("INSERT INTO image(path, activity_id, comment_id)"
                       "VALUES ('%s','%s','%s');" % (filename, new_id, 0))
    category_name=get_category_name(category);
    cursor.execute("INSERT INTO activity(act_id,user_id, title, content,create_time, category, area, reply_times)"
                   "VALUES ('%s','%s','%s','%s','%s','%s','%s', 0);"
                   % (new_id, user_id, title, noise, date, str(category_name), area))

    conn.commit()
    conn.close()
    return new_id
# end of definition of functions

create_form = cgi.FieldStorage()
new_id=insert_activity(create_form)
if(new_id==0):
    print '''
        something really wrong
      </body>
    </html>

    '''
else:
    print '''
    <div style="margin-left:20%;margin-top:50px; font-size:25px; font-family:fantasy;">Successfully create the thread! Redirect to the thread</div>
    '''
    print "<script>setTimeout(function(){window.location.href = 'view_activity.py?id=%d';},3000)</script>" % new_id

    print '''


      </body>
    </html>

    '''







