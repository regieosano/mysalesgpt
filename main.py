from fastapi import FastAPI
from routers import saleschat

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to MySalesGPT!!!"}


@app.get("/favicon.ico")
def favicon():
    return {"message": "Regie's Favicon!"}


app.include_router(saleschat.post_router)
