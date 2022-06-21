import MySQLdb

conn =  MySQLdb.connect(host="localhost" ,database="class_proj" , user="root" , password="" )
cursor = conn.cursor()

    
cursor.execute("select * from user where username = 'rahul' and password = '12345' ")
row = cursor.fetchone()

"""while row is not None :
    print(row)
    row = cursor.fetchone()
"""
print(row)
user1 = row[0]
print(user1)
cursor.close()
conn.close()
