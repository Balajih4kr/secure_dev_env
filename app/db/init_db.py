from .database import Base, engine
from . import models

def init_database():
    models.Base.metadata.create_all(bind=engine)
    print("Database initialized!")

