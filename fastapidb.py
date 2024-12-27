from fastapi import FastAPI ,  HTTPException
from fastapi import Depends

from sqlalchemy import create_engine , Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



app=FastAPI()
# 012 FastAPI Project Connect FastAPI to MySQL https://www.youtube.com/watch?v=yEKZEwKwd7c
# Database configuration
Database="mysql+pymysql://root:root@localhost:3306/python"


# SQLAlchemy setup
engine=create_engine(Database)
sessionLocal = sessionmaker(autocommit=False, autoflush=False , bind=engine)
Base=declarative_base()


class Item(Base):
    __tablename__="Items"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=True)
    lastname=Column(String(50),nullable=False)

# create tables
Base.metadata.create_all(bind=engine)

# Dependancy to get DB session
def get_db():
    db= sessionLocal()
    print(db)
    try:
        yield db
    finally:
        db.close()
#routes
@app.post("/items/")
def create_item(name1: str,lastname1: str=None, db=Depends(get_db)):  
    new_item = Item(name=name1, lastname=lastname1)
    
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
@app.get("/items/{item_id}") 
def read_item(item_id: int ,db=Depends(get_db)):    
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="item not found")
    
    return item 
@app.put("/items/{item_id}")   
def update_data(item_id: int, name: str,lastname: str=None, db=Depends(get_db)): 
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
           raise HTTPException(status_code=404, detail="item not found")
    item.name = name
    item.lastname= lastname
    db.commit()
    return item   
@app.delete("/item/{item_id}")
def delete_item(item_id: int ,db=Depends(get_db)):
    print(dir(db))
    help(db.query)
    item = db.query(Item).filter(Item.id == item_id).first()
    # return {"item":item}
    
    if not item:
            raise HTTPException(status_code=404, detail="item not found")
    db.delete(item)
    db.commit()
    return{"message":"item delete successfully"}








