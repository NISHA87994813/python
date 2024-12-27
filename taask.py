from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI();
list=[]
list1=[]
class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: int
    genre: str

class Author(BaseModel):
        
    id: int
    name: str
    birthdate: int

@app.post("/api/v1/books",status_code=201)
def add_new_book(new_book:Book):
    if new_book:
        list.append(new_book)
        return {"msg":"created successfully","new_book":new_book}#json body
@app.put("/api/v1/books/{id}",status_code=200) 
def update_books(id:int,new_book:Book):
    c=0
    for i in list:
        if i.id==id:  
            list[c]=new_book;
            return {"msg":list}
        c=c+1
    else:
        return{"msg":"not found"}
@app.get("/api/v1/books/{id}")
def display(id:int):
    for i in list:
       
        if i.id==id:
          return {"msg":i}#json body
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")  
        
@app.get("/api/v1/book/all")
def all_bpok():
     return {
          "book":list
     }
@app.delete("/api/v1/books/{id}")
def delete_data(id:int):
    c=0
    for i in list:
          if i.id==id:
            list.pop(c)
            return {"msg":"delete books
                    "}#json body
          c=c+1
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")   
@app.post("/api/v1/new_authors",status_code=201)
def add_new_author(new_author:Author):
    
    if new_author:
          list1.append(new_author)
          return {"msg":"created successfully","new_author":new_author}#json body
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")  
@app.put("/api/v1/authors/{id}",status_code=200) 
def update_authors(id:int,new_author:Author):
    c=0
    for i in list1:
        if i.id==id:  
            list1[c]=new_author;
            return {"msg":list1}
        c=c+1
    else:
        return{"msg":"not found"} 
@app.get("/api/v1/author/all")
def all_author():
     return {
          "book":list1
     } 
@app.get("/api/v1/authors/{id}")
def display(id:int):
    for i in list1:
       
        if i.id==id:
          return {"msg":i}#json body
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")  
@app.delete("/api/v1/authors/{id}")
def delete_data(id:int):
    for i in list1:
          if i.id==id:
            list1.pop(id)
            return {"msg":"delete authors"}#json body
    else:
             raise HTTPException(status_code=500,detail="somthing went wrong")       