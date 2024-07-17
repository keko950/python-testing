from python_testing.domain.contract import Contract
from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path

from python_testing.domain.contract_repository import ContractRepository
from python_testing.repositories.psql_contract_repository import PsqlContractRepository

contracts_router = APIRouter(prefix="/contracts", tags=["contracts"])


@contracts_router.get("/")
async def get_contracts(contract_repository: ContractRepository = Depends(
    PsqlContractRepository)) -> List[Contract]:
    return await contract_repository.get_contracts()


@contracts_router.post("/", status_code=201)
async def create_contract(contract_repository: ContractRepository = Depends(
    PsqlContractRepository),
                          contract: Contract = Body(...)):
    await contract_repository.create_contract(contract)


@contracts_router.get("/{contract_id}")
async def get_contract(contract_repository: ContractRepository = Depends(
    PsqlContractRepository),
                       contract_id: int = Path(
                           title="The contract id")) -> Contract:
    result = await contract_repository.get_contract(contract_id)
    if not result:
        raise HTTPException(detail="Contract not found.", status_code=404)

    return result
