from sqlalchemy.orm import session
from app.src.tables.contract_table import ContractTable
from app.src.models.contract import Contract
from sqlalchemy.ext.asyncio import AsyncSession


class AsyncContractORM:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def insert_contract(self, contract: Contract):
        item = ContractTable(
            contract_id=contract.contract_id,
            contract_type=contract.contract_type,
            name=contract.name
        )
        await self.session.add(item)

    async def get_contract(self, contract_id: int) -> Contract:
        item = await self.session.query(ContractTable).filter_by(contract_id=contract_id).first()
        return Contract(
            contract_id=item.contract_id,
            contract_type=item.contract_type,
            name=item.name
        )
