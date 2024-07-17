from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class BaseModelClass(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


class Contract(BaseModelClass):
    contract_id: Optional[int] = Field(alias="contractId")
    name: str = Field(max_length=20)
    owner: str
    date: datetime
    price: float
