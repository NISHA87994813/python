from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()
list=[]
store=[]
add_cart=[]
class Register(BaseModel):
    name:str
    email:str
    password:str
class Products(BaseModel):
    id:int
    Product_name:str
    Product_price:int
    Product_quentity:int
    Product_categorey:str
@app.post("/api/v1/users/register",status_code=201)
def add_users(users:Register):
    if users:
        list.append(users)
        return{"register":list}
        
    else:
        raise HTTPException(status_code=404,detail="not valid")
@app.post("/api/v1/login",status_code=200)  
def add_login(email:str,password:str):
    for i in list:
        if i.email==email and i.password==password :
            return{"login":i} 
    else:
        raise HTTPException(status_code=404,detail="not valid user login") 
@app.post("/api/v1/products")  
def add_product(new_product:Products):
    if new_product:
        store.append(new_product)
        return{"add_products":"add product"} 
    else:
        raise HTTPException(status_code=404,detail="not add product")
@app.get("/api/v1/products")
def display_product():
    return{"products display":store}  

@app.get("/api/v1/products/{id}") 
def display_product(id:int):
    for i in store:
        if i.id==id:
            return{"products display":i} 
    else:
        raise HTTPException(status_code=404,detail="not found")   
@app.put("/api/v1/products/{id}",status_code=200)  
def update_products(id:int,new_product:Products):
    c=0  
    for i in store:
        if i.id==id:
            store[c]=new_product
            return{"update product":store}
    else:
        raise HTTPException(status_code=404,detail="not update products") 
@app.delete("/api/v1/product/{product_id}")   
def delete_product(id:int): 
    c=0
    for i in  store:
        if i.id==id:
            store.pop(c)
            return{"products delete":"delete product"}
    else:
        raise HTTPException(status_code=404,detail="not found") 
@app.post("/api/v1/cart")
def add_to_cart(user_id:int,product:Products): 
    add_cart.append({"id":user_id,"product":product} )
    return{"id":user_id,"product":product}      

@app.get("/api/v1/cart/{user_id}")
def display_cart(user_id:int):
    for i in add_cart:
        if i["id"]==user_id:
            return{"cart":i}
    else:
        raise HTTPException(status_code=404,detail="not found")    

               
    



    
    



