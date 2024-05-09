from src.models.contract import Contract
from src.repositories.contract import ContractORM

class ContractHandler:
    def __init__(self, db_handler: ContractORM) -> None:
        self.db_handler = db_handler

    def create_contract(self, contract: Contract):
        self.db_handler.insert_contract(contract)

    def retrieve_contract(self, contract_id: int) -> Contract:
        return self.db_handler.get_contract(contract_id)