from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from datetime import datetime
from typing import Optional


class ContractType(Enum):
    CN = "CN"
    SPA = "SPA"


class Contract(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    contract_id: int = Field(alias="contractId")
    name: str = Field()
    contract_type: ContractType = Field(alias="contractType")
    contract_owner: str = Field(alias="contractOwner")
    contract_start_date: datetime = Field(alias="contractStartDate")
    shell_entity: Optional[str] = Field(alias="shellEntity")
    counter_party: Optional[str] = Field(alias="counterParty")
    execution_date: Optional[datetime] = Field(alias="executionDate")
    number_of_cargoes: Optional[int] = Field(alias="numberOfCargoes")
    contract_holder: Optional[str] = Field(alias="contractHolder")
    created_by: str = Field(alias="createdBy")
    parent_contract_nickname: Optional[str] = Field(alias="parentContractNickname")
    # moar fields
