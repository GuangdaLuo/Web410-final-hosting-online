#!C:\Python27\python.exe







import sqlite3
import hashlib
import datetime
conn = sqlite3.connect('hangout.db')
cursor = conn.cursor()

# create user information table
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('CREATE TABLE IF NOT EXISTS user(user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', username varchar(100), password varchar(100), email varchar(100), create_time varchar(100)'
               ', transid varchar(100))')

# create activity table
cursor.execute('DROP TABLE IF EXISTS activity')
cursor.execute('CREATE TABLE IF NOT EXISTS activity(act_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', user_id INTEGER NOT NULL, title varchar(100), content varchar(2000), create_time varchar(100)'
               ', category varchar(30), area varchar(30), reply_times INTERGER)')

# create comment table
cursor.execute('DROP TABLE IF EXISTS comment')
cursor.execute('CREATE TABLE IF NOT EXISTS comment(com_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', activity_id INTEGER, content varchar(2000), create_time varchar(100), replier_id INTEGER, replier_name varchar(100))')

# create participants table
cursor.execute('DROP TABLE IF EXISTS participants')
cursor.execute('CREATE TABLE IF NOT EXISTS participants( activity_id INTEGER, user_id INTEGER)')

# create image table
cursor.execute('DROP TABLE IF EXISTS image')
cursor.execute('CREATE TABLE IF NOT EXISTS image(img_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', path varchar(256), activity_id INTEGER, comment_id INTEGER)')

#create security code table
cursor.execute('DROP TABLE IF EXISTS sec_code')
cursor.execute('CREATE TABLE IF NOT EXISTS sec_code(code_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
               ', username varchar(100), security_code varchar(100))')

conn.commit()

date = str(datetime.datetime.now())
hasher = hashlib.md5()
hasher.update('123123')
hasher.update(date)
encrypted = hasher.hexdigest()
cursor.execute("INSERT INTO user(user_id, username, password, create_time) VALUES('1','admin','%s','%s');"
               % (encrypted, date))
# insert two sample activity
cursor.execute("INSERT INTO activity(act_id,user_id, title, content,create_time, category, area, reply_times)"
                   "VALUES ('1','1','first activity ever','hello from hangout1','%s','sport','NY', 1);" % (date))
cursor.execute("INSERT INTO activity(act_id,user_id, title, content,create_time, category, area, reply_times)"
                   "VALUES ('2','1','second activity ever','hello again from hangout1','%s','travel','AL', 0);" % (date))
cursor.execute("INSERT INTO activity(act_id,user_id, title, content,create_time, category, area, reply_times)"
                   "VALUES ('3','1','third activity ever','hello one more time from hangout1','%s','game','NY', 0);" % (date))
# cursor.execute("INSERT INTO image(path, activity_id, comment_id)"
#                "VALUES ('1.jpg','1','0');")

# insert some images
cursor.execute("insert into image(img_id, path, activity_id) VALUES ('1', 'slide1.jpg', '1');")
cursor.execute("insert into image(img_id, path, activity_id) VALUES ('2', 'slide2.jpg', '2');")
cursor.execute("insert into image(img_id, path, activity_id) VALUES ('3', 'slide3.jpg', '3');")
# insert some comments
cursor.execute("insert into comment(com_id, activity_id, content, create_time, replier_id, replier_name)"
                "VALUES ('1', '1', 'Hello from comment', '%s', '1', 'admin');" % (date))

conn.commit()
conn.close()


