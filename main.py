from fastapi import FastAPI
from routes import checkRouter

app = FastAPI()

app.include_router(checkRouter.router)

