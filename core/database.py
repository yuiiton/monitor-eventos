from sqlmodel import Session, SQLModel, create_engine

DATABASE_URL = "sqlite:///data/monitor.db"

engine = create_engine(DATABASE_URL)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine, expire_on_commit=False)