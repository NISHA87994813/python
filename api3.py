from fastapi import FastAPI
app1=FastAPI();
list=[]

@app1.get("/")
def display():
    return{"list":list}
@app1.post("/") 
def add(new_values):
    list.append(new_values)
    return{"msg": "add values"}
@app1.put("/")  
def update(old_values,new_values):
    if old_values in list:
        list.update(old_values)
        k=list.index(old_valus)
        list[k] = new_value
        return{"msg":"value updated"}
    else:
         return{"msg":"value not  updated"}
@app1.delete("/") 
def delete( values):
    if values in list:
        list.remove(values)
        return{"msg":"value delete"}
    else:
        return{"msg":"value not delete"}
    