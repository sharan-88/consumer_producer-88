from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "sqlite:///./products.db"
engine = create_engine(DATABASE_URL)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
