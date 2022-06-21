import MySQLdb

conn =  MySQLdb.connect(host="localhost" ,database="class_proj" , user="root" , password="" )
cursor = conn.cursor()
ins = "INSERT INTO `user` (`Username`, `gmail`, `Password`, `Fname`, `Mname`, `Lname`)  "
val = " VALUES ('ghdghghh', 'ghgh', 'ghgh', 'dghhd', 'ghgh', 'dghdgh');"
sql = ins + val
try :
    cursor.execute(sql)
    conn.commit()
except:
    conn.rollback()

cursor.close()
conn.close()
