from sqlalchemy.orm import session
from app.src.tables.contract_table import ContractTable
from app.src.models.contract import Contract


class ContractORM:
    def __init__(self, session: session.Session):
        self.session = session

    def insert_contract(self, contract: Contract):
        item = ContractTable(
            contract_id=contract.contract_id,
            contract_type=contract.contract_type,
            name=contract.name
        )
        self.session.add(item)

    def get_contract(self, contract_id: int) -> Contract:
        item = self.session.query(ContractTable).filter_by(contract_id=contract_id).first()
        return Contract(
            contract_id=item.contract_id,
            contract_type=item.contract_type,
            name=item.name
        )
