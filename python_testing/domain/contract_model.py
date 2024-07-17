from python_testing.domain.contract import Contract as ContractSchema
from sqlalchemy import DateTime, Float, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contract(Base):
    __tablename__ = "contract"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    owner = Column(String)
    date = Column(DateTime)
    price = Column(Float)

    def to_contract(self) -> ContractSchema:
        return ContractSchema(contractId=self.id,
                              date=self.date,
                              name=self.name,
                              owner=self.owner,
                              price=self.price)
