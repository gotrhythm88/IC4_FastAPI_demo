from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item}")
def read_root(item: int):
    return {"Hello": "World", "item_id": item}