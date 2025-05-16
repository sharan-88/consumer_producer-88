from models import Customer

def createProduct(data,session):
    cust= Customer(**data.model_dump())
    session.add(cust)
    session.commit()
    session.refresh(cust)
    return cust


