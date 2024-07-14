from fastapi import FastAPI, APIRouter
router_main = APIRouter()

@router_main.get("/")
async def root():
    return {"message": "Hello World"}

@router_main.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
