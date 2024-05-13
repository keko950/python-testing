from src.models.contract import Contract
from src.controllers.contract import ContractHandler
from src.repositories.contract import ContractORM

from fastapi import FastAPI

app = FastAPI()
orm = ContractORM()
handler = ContractHandler(orm)

@app.get("/")
async def get_contract(id: int):
    return handler.retrieve_contract(id) 

app.post("/")
async def post_contract(contract: Contract):
    handler.create_contract(contract)