from fastapi import Depends
from sqlalchemy.orm import Session
from python_testing.domain.contract_repository import ContractRepository
from python_testing.domain.contract import Contract
from python_testing.domain.contract_model import Contract as ContractDB
import psycopg2

from python_testing.dependencies.database import get_db
from typing import List, Optional


class PsqlContractRepository(ContractRepository):
    def __init__(self, db_session: Session = Depends(get_db)):
        self.session = db_session

    async def get_contracts(self) -> List[Contract]:
        res = self.session.query(ContractDB).all()
        return [item.to_contract() for item in res]

    async def get_contract(self, contract_id: int) -> Optional[Contract]:
        item = self.session.query(ContractDB).filter_by(id=contract_id).first()
        if item:
            return item.to_contract()

    async def create_contract(self, contract: Contract):
        item = ContractDB(name=contract.name,
                          owner=contract.owner,
                          date=contract.date,
                          price=contract.price)
        self.session.add(item)

        self.session.commit()

    async def remove_contract(self, contract_id: int):
        item = self.session.query(ContractDB).filter_by(id=contract_id).first()
        self.session.delete(item)

        self.session.commit()
