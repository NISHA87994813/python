from fastapi import FastAPI
app=FastAPI();
list=[]
@app.get("/display")
def display():
    return{"list":list}
@app.post("/add/{variable}")
def add(variable):
    list.append(variable)
    return{"list":"values added"} 
@app.delete("/delete/{variable}")
def dilit(variable):
    if variable in list:
        list.remove(variable)
        return{"msg":"values deleted"} 
    else:
        return{"msg":"value not found"}
@app.put("/update/{variable}")
def update(old_value,new_value):
    if old_value in list:
        k = list.index(old_value)
        list[k] = new_value
        return{"msg":"value updated"}
    else:
        return{"msg":"value not found"}
        
    











