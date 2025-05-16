from fastapi import Depends, FastAPI
from sqlmodel import Session, select
from datbase import create_db,provide_sess
from models import Customer,customer_input
from crud import createProduct

create_db()

app =FastAPI()

@app.get("/")
def root_customer():
    return{"message":"this is just a message"}

@app.post("/customers/",response_model=Customer)
def create_product(data:customer_input,session:Session=Depends(provide_sess)):
    return createProduct(data,session)


@app.get("/customers/")
def get_product(session:Session=Depends(provide_sess)):
    return session.exec(select(Customer)).all()