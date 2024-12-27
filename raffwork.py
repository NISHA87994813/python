from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
list=[]
class Student(BaseModel):
    id:int
    name:str
    age:int
    Class:int
    subject:str
@app.get("/Get/students/",status_code=200)  
def display_student(): 
    return{"msg":list}
@app.get("/Get/students/{id}",status_code=200)
def display_student(id:int):
    for i in list:
        if i.id==id:
                  return {"msg":i}#json body
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")  
@app.post("/Post/students/")
def add_student(new_student:Student):
      if new_student:
            list.append(new_student)
            return{"msg":"create successfully","new_student":new_student}
      else:
            return{"msg":"not post"}
@app.put("/Put/update/") 
def update_student(id:int,new_student:Student):   
      c=0
      for i in list:
            if i.id==id:
                  list[c]=new_student
                  return{"msg":list}
            c=c+1
      else:
            return{"msg":"not update"} 
@app.delete("/Delete/student/{id}")  
def delete_student(id:int): 
      c=0
      for i in list:
            if i.id==id:
                  list.pop(c) 
                  return {"msg":"delete student"}#json body
            c=c+1
      else:
             raise HTTPException(status_code=500,detail="somthing went wrong")          


    