from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine , Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# FastAPI app
app = FastAPI()

# Database configuration
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/database_name"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the model
class Item(Base):
    _tablename_ = "Items"
    id = Column(Integer, primary_key=True, index=True)
    name1 = Column(String(100), nullable=False)
    description1 = Column(String(255), nullable=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/items/")
def create_item(name: str, description: str = None, db=Depends(get_db)):
    new_item = Item(name1=name, description1=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.get("/items/{item_id}")
def read_item(item_id: int, db=Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, description: str = None, db=Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = name
    item.description = description
    db.commit()
    return item

@app.delete("/items/{item_id}")
def delete_item(item_id: int, db=Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": "Item deleted successfully"}