from fastapi import FastAPI
from routes import checkRouter, productRouter
from sqlmodel import SQLModel
from models import *
from database import db

SQLModel.metadata.create_all(db.engine)

app = FastAPI()

app.include_router(checkRouter.router)
app.include_router(productRouter.router)
