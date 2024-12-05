from fastapi import FastAPI
app2=FastAPI();
list=[]
@app2.get("/display")
def display():
    return{"msg":list}
@app2.post("/add/{values_add}") 
def add(values_add):
    list.append(values_add)
    return{"msg":"values add"}
@app2.put("/update/{o_values}/{n_values}") 
def update(o_values,n_values):
    if o_values in list:
       k=list.index(o_values)
       list[k]=n_values
       return{"msg":"update values"}
    else:
        return{"msg":"not update"}
@app2.delete("/delete/{values_delete}") 
def delete(values_delete):
        if values_delete in list:
            list.remove(values_delete)
            return{"msg":"delete values"}
        else:
            return{"msg":" not delete"}
        
        
   