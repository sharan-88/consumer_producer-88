from sqlmodel import SQLModel, Session, create_engine # type: ignore

DATABASE_URL = "sqlite:///./customer.db"
engine= create_engine(DATABASE_URL)

def create_db():
    SQLModel.metadata.create_all(engine)

def provide_sess():
    with Session(engine) as session:
        yield session    