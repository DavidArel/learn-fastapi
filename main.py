
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

# bisa set optional class pakai ini
from typing import List, Optional

# import session
from database import SessionLocal
import models

app = FastAPI()

#create object
class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    isActive:bool

    class Config:
        orm_mode=True

# init db
db = SessionLocal()

@app.get('/')
def index():
    return {"Message":"Hello World first!"}

@app.get('/greet/{name}')
def greet_name(name:str): #pass tipe
    return {"greeting":f"Hello {name}"}

# contoh implementasi optional
@app.get('/greet')
def greet_optional(name:Optional[str]="user"): #"user" is a default val 
    return {"message": f"hello optional {name}"}


# create all routes for item related operation
@app.get('/items', response_model=List[Item], status_code=200)
def get_all_item():
    items = db.query(models.Item).all()
    return items
    # pass

@app.get('/item/{id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(id:int):
    item = db.query(models.Item).filter(models.Item.id == id).first()

    return item

@app.post('/items', response_model=Item, 
        status_code=status.HTTP_201_CREATED)
def create_item(item:Item):
    new_item = models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        isActive=item.isActive
    )

    # exceptions
    db_item = db.query(models.Item).filter(models.Item.name==new_item.name).first()
    print(db_item)
    if db_item is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="failed")

    db.add(new_item)
    db.commit()

    return new_item
    # pass

@app.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_201_CREATED)
def update_item(item_id:int, item:Item):
    item_db = db.query(models.Item).filter(models.Item.id==item_id).first()
    item_db.name = item.name
    item_db.price = item.price
    item_db.description = item.description
    item_db.isActive = item.isActive

    db.commit()
    return item_db
    # pass

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="id not found")

    db.delete(item_to_delete)
    db.commit()
    
    return item_to_delete
    # pass

