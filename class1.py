from fastapi import FastAPI
from pydantic import BaseModel
class Emp(BaseModel):
    name :str
    age :int
    sal :int

lst=[]
app=FastAPI();
@app.post("/")
def add_data(e:Emp):
    lst.append(e)
    return{"msg":"data added..!"}

@app.get("/")
def display():    
    return {"msg":lst}
 
@app.delete("/")
def delete(name:str):
        z =0
        for i in lst:
            if i.name == name:
                lst.pop(z)
            
            
                return {"msg":"deleted"}
            z=z+1
        else:
            return {"msg":"not found deleted"}
@app.put("/") 
def update(name:str,n_name:str):
    
    for i in lst:
        if i.name==name:
            i.name = n_name
            
            return{"msg":"  putupdate values"}
            
    else:
        return{"msg":"put not update"}
            