import sqlite3
from datetime import datetime


users = sqlite3.connect("users_data")
"""users.execute("INSERT INTO user1 values('hellloooo','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('bye','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('bye','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('bye','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('hellloooo','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('hellloooo','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user1 values('hellloooo','user3','"+str(datetime.now())+"')")
users.execute("INSERT INTO user2 values('hellloooo','user3','"+str(datetime.now())+"')")"""
users.commit()
for item in users.execute("SELECT * FROM user3 ").fetchall():
    print (item)
print ("done")

users.close()

