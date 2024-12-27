from fastapi import FastAPI
names=[]
app=FastAPI();
@app.get("/display")
def getuser():
    return{"names":names}
@app.post("/adduser/{name}")
def postusers(name:str):
    names.append(name)
    return{"names":"add users"}
@app.delete("/update/{name}")
def deleteusers(name:str):
    try:
        names.remove(name)
        return{"names":"delete users"}
    except:
        return{"names":"not delete users"}
@app.put("/delete/{name}")    
def updateusers(old_name:str,new_name:str):
    try:
        i=names.index(old_name)
        names.remove(old_name)
        names.insert(i,new_name)
        return{"names":" update  names"}    
    except:
        return{"names":old_name+"not found"}    