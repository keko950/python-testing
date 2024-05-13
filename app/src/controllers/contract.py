from app.src.models.contract import Contract
from app.src.repositories.contract import ContractORM
import requests


class ContractHandler:
    def __init__(self, db_handler: ContractORM) -> None:
        self.db_handler = db_handler

    def create_contract(self, contract: Contract):
        self.db_handler.insert_contract(contract)

    def retrieve_contract(self, contract_id: int) -> Contract:
        return self.db_handler.get_contract(contract_id)

    def verify_contract(self, contract_id) -> bool:
        contract = self.retrieve_contract(contract_id)
        response = requests.get(
            f"https://someapi.com/verify/{contract.contract_id}", data=contract.dict())

        return response.status_code == 200
