from app.src.models.contract import Contract
from app.src.repositories.async_contract import AsyncContractORM
import requests
import httpx


class AsyncContractHandler:
    def __init__(self, db_handler: AsyncContractORM) -> None:
        self.db_handler = db_handler

    async def create_contract(self, contract: Contract):
        await self.db_handler.insert_contract(contract)

    async def retrieve_contract(self, contract_id: int) -> Contract:
        return await self.db_handler.get_contract(contract_id)

    async def verify_contract(self, contract_id) -> bool:
        contract = await self.retrieve_contract(contract_id)
        async with httpx.AsyncClient() as client:
            response = await client.post(f"https://someapi.com/verify/{contract.contract_id}", content=contract.model_dump())

            return response.status_code == 200
