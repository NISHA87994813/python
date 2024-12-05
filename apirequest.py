from fastapi import FastAPi
app=FastAPi();
list=[]
@app.get("/")
def display(name):
    return{"msg":"successfully"}
@app.post("/") 
def add(values_add):
    list.append(values_add)
    return{"msg":"values add"}  
@app.put("/") 
def update(o_values,n_values):
    if o_values in list:
       a=list.index(o_values)
       list[a]=n_values
       
       return{"msg":"  putupdate values"}
    else:
        return{"msg":"put not update"}    
@app.delete("/")
def delete(delete_values)  :
        if delete_values in list:
            list.remove(delete_values)
            return{"msg":"delete values"}
        else:
            return{"msg":"not delete"}