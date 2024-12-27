from fastapi import FastAPI, HTTPException
from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy import create_engine,Integer,String,Column,Date,ForeignKey
from sqlalchemy.ext.declarative  import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import date
app=FastAPI()
Database="mysql+pymysql://root:root@localhost:3306/python"
engine=create_engine(Database)
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

class Author(Base):
    __tablename__ = "Author"
    id = Column(Integer,autoincrement=True,primary_key=True)  # Primary Key added
    author_name = Column(String(50), unique=True, nullable=False)  # Non-nullable and unique
    birth_date = Column(Date, nullable=True)  # Default to current date

    # Relationship to books
    books = relationship("Book", back_populates="author", cascade="all, delete")

class Author_without_db(BaseModel):
        
    author_name: str
    birth_date: date



class Book(Base):  
    __tablename__ = "Book"
    id = Column(Integer,autoincrement=True, primary_key=True)
    title = Column(String(50), nullable=False)
    author_name =  Column(String(50), ForeignKey("Author.author_name"), nullable=False)
    publish_date = Column(Date, nullable=False)
    gener = Column(String(50), nullable=False)  # Fixed typo in 'gener'

    # Relationship to author
    author = relationship("Author", back_populates="books") 
class Bookr_without_db(BaseModel):
    
    title: str
    author_name: str
    publish_date: date
    gener: str

Base.metadata.create_all(bind=engine)


def get_db():
           db=sessionLocal()
           print(db)
           try:
                yield db
           finally:
                db.close()  

@app.post("/api/v1/books",status_code=201)  
def create_book(obj:Bookr_without_db,db=Depends(get_db)):
     new_book=Book(**obj.dict())     
     db.add(new_book)
     db.commit()
     db.refresh(new_book)
     return new_book

@app.post("/api/v1/authors",status_code=201)
def create_author(obj:Author_without_db,db=Depends(get_db)):
      new_authors=Author(**obj.dict())
      db.add(new_authors)
      db.commit()
      db.refresh(new_authors)
      return new_authors
@app.get("/api/v1/authors/{id}")
def read_author(id:int,db=Depends(get_db)):
      authors=db.query(Author).filter(Author.id==id).first()
      if not authors:
            raise HTTPException(status_code=404,detail="not found")
      return {
        "id": authors.id,
        "name": authors.author_name,
        "birth_date":authors.birth_date,
        "books": [{"id": book.id, "title": book.title,"publish_date":book.publish_date,"gener":book.gener} for book in authors.books],
 }
@app.get("/api/v1/books/{id}")
def read_book(id:int,db=Depends(get_db)):
      books=db.query(Book).filter(Book.id==id).first()
      if not books:
                   raise HTTPException(status_code=404,detail="not found")
      return {
        "id": books.id,
        "title": books.title,
        "author": {"id": books.author.id, "name": books.author.author_name,"birth_date":books.author.birth_date,"publish_date":books.publish_date,"gener":books.gener},}


@app.put("/api/v1/books/{id}",status_code=200)
def update_books(id:int,title:str,author_name:str,publish_date:date,gener:str=None,db=Depends(get_db)):
         book = db.query(Book).filter(Book.id == id).first()
         if not book:
                 
                 raise HTTPException(status_code=404,detail="not found")
         book.title=title
         book.auhtor_name=author_name
         book.publish_date=publish_date
         book.gener=gener
         db.commit()   
         return book
 
@app.put("/api/v1/authors/{id}",status_code=200)
def update_author(id:int,name:str,birth_date:date=None,db=Depends(get_db)):
      authors = db.query(Author).filter(Author.id == id).first()
      if not authors:

            raise HTTPException(status_code=404,detail="not found")
      authors.author_name=name
      authors.birth_date=birth_date
      db.commit()   
      return {"msg":authors}

@app.delete("/book/{book_id}")
def delete_book(book_id: int ,db=Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    # return {"item":item}
    
    if not book:
            raise HTTPException(status_code=404, detail="book not found")
    db.delete(book)
    db.commit()
    return{"message":" delete successfully"}

@app.delete("/author/{author_id}")
def delete_book(author_id: int ,db=Depends(get_db)):
    author = db.query(Author).filter(Author.id == author_id).first()
    
    
    if not author:
            raise HTTPException(status_code=404, detail=" not found")
    db.delete(author)
    db.commit()
    return{"message":" delete successfully"}
