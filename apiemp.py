from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI();
lst=[]
class Emp(BaseModel):
    name: str
    age: int
    address: str
    email: str
    password: str

class Medical(BaseModel):
    blood: str
    des: str
@app.post("/")
def add_data(e:Emp,m:Medical):
        x={"employe":e,"medical":m}
        lst.append(x)
        return{"msg":"data added..!"}
@app.put("/")
def update_data(e:Emp,new_Emp:Emp):
    z=0
    for i in lst:
        if i["name"].name ==e.name:
            i=new_Emp
            break
        z=z+1
    else:
        return {"not found"}
@app.delete("/")    
def Delete_data(name:str):
        z =0
        for i in lst:
            if i["employe"].name==name:
                lst.pop(z) 
                return {"msg":"deleted"}
            z=z+1
        else:
            return {"msg":"not found deleted"}
@app.get("/")
def display():
     return{"msg":lst}

        
    