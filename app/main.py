from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from app import service, models, schema, database

app = FastAPI()

def get_db():
    db = database.Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return RedirectResponse(url="/items/")

@app.get("/items/")
async def get_items(db: Session = Depends(get_db)):
    items = service.get_items(db)
    return items

@app.get("/items/{item_id}")
async def get_item(item_id: int, db: Session = Depends(get_db)):
    item = service.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items/")
async def create_item(item: schema.ItemCreate, db: Session = Depends(get_db)):
    db_item = service.create_item(db, item)
    return db_item

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: schema.ItemCreate, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = service.update_item(db, db_item, updated_item)
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = service.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    service.delete_item(db, db_item)
    return {"message": "Item deleted successfully"}