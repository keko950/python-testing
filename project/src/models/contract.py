from pydantic import BaseModel, Field
from enum import Enum

class ContractType(Enum):
    CN = "CN"
    SPA = "SPA"

class Contract(BaseModel):
    contract_id: int = Field(alias="contractId")
    name: str = Field()
    contract_type: ContractType = Field(alias="contractType")
    # moar fields 
