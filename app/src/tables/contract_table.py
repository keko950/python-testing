from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class ContractTable(Base):
    __tablename__ = "contract"
    __table_args__ = {"schema": "some_schema"}

    contract_id = Column(Integer, primary_key=True)
    contract_type = Column(String)
    name = Column(String)
