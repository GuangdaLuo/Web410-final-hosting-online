#!C:\Python27\python.exe





import sqlite3

conn = sqlite3.connect('hangout.db')
cursor = conn.cursor()
results = cursor.execute("SELECT * FROM user;")
print "user"
for r in results:
    print r


results = cursor.execute("SELECT * FROM activity;")
print "activity"
for r in results:
    print r

results = cursor.execute("SELECT * FROM image;")
print "image"
for r in results:
    print r
results = cursor.execute("SELECT * FROM sec_code;")
print "sec_code"
for r in results:
    print r
results = cursor.execute("SELECT * FROM comment;")
print "comment"
for r in results:
    print r
conn.close()