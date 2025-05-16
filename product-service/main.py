from fastapi import FastAPI, Depends
from database import create_db, get_session
from models import Product
import crud
from sqlmodel import Session
create_db()
app = FastAPI(title="Product Service")

@app.get("/")
def root():
    return{"message":"product service is working"}

@app.post("/products/")
def create(product: Product, session: Session = Depends(get_session)):
    return crud.create_product(session, product)

@app.get("/products/")
def list_all(session: Session = Depends(get_session)):
    return crud.get_products(session)
