from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"mensaje": "Hola mundo"}
@app.get("/info")
def info():
    return {"info": "Hola 2"}