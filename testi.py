import mysql.connector as mc
from fastapi import FastAPI
app=FastAPI()



c = mc.connect(host="localhost",user="root",password="root",database="python")
x = c.cursor()
@app.post("/") 
def add(fname,lname):
    
    Q="insert into stud(name,lastname) values('"+fname+"','"+lname+"')"
    x.execute(Q)
    c.commit();
    return{"msg":"values add"}  
@app.delete("/")
def delete(fname)  :
        
               Q="delete from stud where name='"+fname+"'";
               x.execute(Q)
               c.commit()
               return{"msg":"delete values"}
@app.put("/") 
def update(o_fname,nfname):
        Q="update stud SET name='"+nfname+"' WHERE name='"+o_fname+"'";
        x.execute(Q)
      
        c.commit()      
        return{"msg":"  putupdate values"}


      
@app.get("/")
def display():
    Q="select * from  stud"
    x.execute(Q)
    z = x.fetchall()
    return{"msg"}
               