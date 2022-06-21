import MySQLdb

tlist=[]
slist=[]


conn =  MySQLdb.connect(host="localhost" ,database="class_proj" , user="root" , password="" )
cursor = conn.cursor()

cursor.execute("SELECT * FROM `course` WHERE username = 'rahul' ")
row = cursor.fetchone()

while row is not None :
    slist.append(row)
    row = cursor.fetchone()


cursor.execute("SELECT * FROM `subject` WHERE username='rahul' ")
row1 = cursor.fetchone()

while row1 is not None :
    tlist.append(row1)
    row1 = cursor.fetchone()
print(slist, tlist)
cursor.close()
conn.close()

