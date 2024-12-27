from flask import Flask

app = Flask(__name__)
lst = []
# @app.route("/")
# def hello_world():
#     lst.append()
#     return {"Hello": "World!"}

# @app.route("/nisha")
# def world():
#     return {"Hello": "nisha"}

# @app.route("/nisha1/<z>")
# def world1(z):

#     return{"msg":z}



@app.route("/add/<int:data>")
def add(data:int):
    lst.append(data)
    return{"msg":"data added..."}

@app.route("/get")
def get():
    
    return{"msg":lst}

@app.route("/delete/<int:value>")
def delete(value:int):
    if value in lst:
        lst.remove(value)
        return{"msg":"deletded succesfully"}
    else:
        return{"msg":"not found..."}

@app.route("/update/<int:oldvalue>/<int:newvalue>")
def update(oldvalue:int,newvalue:int):
    if oldvalue in lst:
        index=lst.index(oldvalue)
        lst[index] = newvalue
        return{"msg":"update succesfully"}
    else:
        return{"msg":"not found..."}



