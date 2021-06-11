from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Mi primera practica": "Soy Jorge"}


@app.get("/test/{use_id}")
def read_item(use_id: int, key: str = None):
    return {"use_id": use_id, "key": key}