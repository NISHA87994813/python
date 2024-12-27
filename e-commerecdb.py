from fastapi import FastAPI,HTTPException
from fastapi import Depends
from pydantic import BaseModel
from typing import Optional

from sqlalchemy import create_engine,Integer,String,Column,ForeignKey
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
app=FastAPI( title="My FastAPI Application",
    description="This is a description of my FastAPI application")
Database="mysql+pymysql://root:root@localhost:3306/python"
engine=create_engine(Database)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
class User(Base):
    __tablename__ = "User"
    id = Column(Integer,autoincrement=True,primary_key=True)  # Primary Key added
    name=Column(String(50),nullable=False)
    email = Column(String(50),nullable=False,unique=True)  # Non-nullable and unique
    password= Column(String(50), nullable=True)  # Default to current date
  
    products = relationship('Product', back_populates='user')
class add_to_cartdb(Base):
    __tablename__ = "add_to_cart"
    id=Column(Integer,autoincrement=True,primary_key=True)  
    users_id = Column(Integer)  # Primary Key added
    products_id=Column(Integer)  
  
    
class Add_to_cart(BaseModel):
    product_id :int
    user_id :int

class Users_db(BaseModel):
    name:str
    email:str
    password:str=None
    


class Product(Base):  
    __tablename__ = "Products"
    id = Column(Integer,autoincrement=True, primary_key=True)
    product_name = Column(String(50),  nullable=False)
    product_price =  Column(Integer,  nullable=False)
    product_quentity = Column(Integer, nullable=False)
    product_categorey = Column(String(50), nullable=False)  # Fixed typo in 'gener'
    user_id = Column(Integer, ForeignKey('User.id'), default=True,nullable=False) 
  
    user = relationship('User', back_populates='products')
class Products_db(BaseModel):

    product_name:str
    product_price:int
    product_quentity:int
    product_categorey:str

Base.metadata.create_all(bind=engine)    
    
def get_db():
           db=sessionLocal()
           print(db)
           try:
                yield db
           finally:
                db.close()  

@app.post("/api/v1/user",status_code=201)  
def create_user(obj:Users_db,db=Depends(get_db)):
    '''add new users'''
    try:
        if(obj.name =="" or obj.email =="" or  obj.password ==""):
            print("hello")
            raise ZeroDivisionError
        
        new_user=User(**obj.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except ZeroDivisionError:
        return HTTPException(status_code=406,detail="must be fill")
         
    except:
        return HTTPException(status_code=500,detail="somthing went wrong")
    
@app.post("/api/v1/products",status_code=201)
def create_products(obj:Products_db,db=Depends(get_db)):
    ''''ad new product'''
    try:
        if(obj.product_name=="" or obj.product_price =="" or  obj.product_quentity =="" or obj.product_categorey):
            print("hello")
            raise ZeroDivisionError

        new_products=Product(**obj.dict())
        db.add(new_products)
        db.commit()
        db.refresh(new_products)
        return new_products
    except ZeroDivisionError:
             return HTTPException(status_code=406,detail="must be fill")

    except:
           return HTTPException(status_code=500,detail="somthing went wrong")

@app.put("/api/v1/user", status_code=200)
def update_user(user_id: Optional[int] =None , obj:Optional[ Users_db]=None, db = Depends(get_db)):
    '''update user'''
    
    try:
            if user_id is None or obj is None:
                raise IndexError 
    
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                 raise IndexError
    
            user.email = obj.email
            user.name = obj.name
            user.password = obj.password
            db.commit()
            db.refresh(user)
            return user
    except IndexError:
             return HTTPException(status_code=406,detail="must be fill")

    except:
           return HTTPException(status_code=500,detail="somthing went wrong")

@app.put("/api/v1/product/{product_id}", status_code=200)
def update_user(product_id: int, obj: Products_db, db = Depends(get_db)):
    '''update product with id'''

    try:
        if product_id is None or obj is None:
            raise IndexError 

        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=" not found")
        Product.product_name=obj.name
        Product.product_price=obj.price
        Product.product_categorey=obj.categorey
        Product.product_quentity=obj.quentity
        db.commit()
        db.refresh(product)
        return product
    except IndexError:
        return HTTPException(status_code=406,detail="must be fill")

    except:
        return HTTPException(status_code=500,detail="somthing went wrong")

@app.delete("/api/v1/product/{product_id}")
def delete_book(product_id: int ,db=Depends(get_db)):
    '''delete product with id'''
    product = db.query(Product).filter(Product.id == product_id).first()
    # return {"item":item}
    
    if not product:
            raise HTTPException(status_code=404, detail="book not found")
    db.delete(product)
    db.commit()
    return{"message":" delete successfully"}

@app.post("/api/v1/product/{product_id}")
def add_cart(obj:Add_to_cart,db=Depends(get_db)):
        if  obj.product_id<0 or obj.user_id<0 :
             return {"msg":"not valid"}
        else:
            addtocart = Add_to_cart(**obj.dict())

            db.add(addtocart)
            db.commit()
            db.refresh()
            return{"msg":"added...!"}
