import mysql.connector as mc
c = mc.connect(host="localhost",user="root",password="root",database="python")
#id = int(input())
#name = input()
#lname = input()

#a="hello"
#b="buy"
#print(a+b)

#Q = "insert into py1 values(4,'ddd','vvv');"
# A = "UPDATE py1 SET name='disha' WHERE id=2;"
#s="insert into py1 values('"+str(id)+"','"+name+"','"+lname+"');
#d="delete from py1 where name ='ddd'";
cursor = c.cursor()
query = "SELECT * FROM py1"
cursor.execute(query)

record = cursor.fetchall()
print("Fetched record: ", record)
#x = cursor()


#x = c.cursor()

#x.execute(d)
#x.execute(s)
#print(dir(x))
# x.execute(A)
#x.execute(Q)
#c.commit();#save
#print(dir(c))