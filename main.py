from fastapi import FastAPI
from bs import productos

app = FastAPI()

@app.get('/')
async def hello_world(): 
    return {"helo": "olarata"}

@app.post('/post/{cedula}')
async def post(cedula): 
    return {"cedula": {cedula}}

@app.get('/bs')
async def basedatos(): 
    return {"basedatos": productos[-2]}