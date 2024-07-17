from abc import ABC
from typing import List, Optional
from python_testing.domain.contract import Contract


class ContractRepository(ABC):
    async def get_contracts(self) -> List[Contract]:
        raise NotImplementedError

    async def get_contract(self, contract_id: int) -> Optional[Contract]:
        raise NotImplementedError

    async def create_contract(self, contract: Contract):
        raise NotImplementedError

    async def remove_contract(self, contract_id: int):
        raise NotImplementedError
