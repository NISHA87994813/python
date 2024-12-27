from flask import Flask

app = Flask(__name__)
lst = []

class Book():
    def __init__(self,name,price):
        self.name = name
        self.price= price




@app.route("/add/<name>/<price>")
def add_new_book(name:str, price:int):
    new_book = Book(name,price)
    # new_book.name = name
    # new_book.price = price
    lst.append(new_book)
    return {"msg":"created successfully","new_book":[new_book.name,new_book.price]}
@app.route("/delete/<name>")
def delete(name:str):
    c=0
    for i in lst:
        if i.name == name:
            lst.pop(c)
            return{"msg":"deletded succesfully"}
        c=c+1
    else:
        return{"msg":"not found..."}
@app.route("/update/<oldname>/<newname>")
def update(oldname:str,newname:str):
    for i in lst:
        if i.name == oldname:
            i.name = newname
        
        return{"msg":"update succesfully"}
    else:
        return{"msg":"not found..."}
    
@app.route("/get")   
def get():
    data =[]
    c=0
    for i in lst:
       dic={}
       dic[c]=[i.name,i.price]
       data.append(dic)
    return data