from unittest.mock import AsyncMock, Mock, patch
import pytest
from datetime import datetime
from app.src.controllers.contract import ContractHandler
from app.src.controllers.async_contract import AsyncContractHandler
from app.src.models.contract import Contract, ContractType
import httpx
from polyfactory.factories.pydantic_factory import ModelFactory 
from polyfactory.fields import Ignore

class ContractFactory(ModelFactory[Contract]):
    __model__ = Contract

    contract_owner = ModelFactory.__random__.choice(["gibe", "gab", "gob"])
    number_of_cargoes = ModelFactory.__random__.randint(1, 100)

@pytest.fixture(scope="module")
def contract_fixture():
    print("called before each test file")
    return ContractFactory.build()

def test_create_contract(contract_fixture):
    orm = Mock()
    orm.insert_contract = Mock(return_value=True)
    handler = ContractHandler(orm)
    handler.create_contract(contract_fixture)
    orm.insert_contract.assert_called_once_with(contract_fixture)


def test_retrieve_contract(contract_fixture, test_fixture):
    orm = Mock()
    orm.get_contract = Mock(return_value=contract_fixture)
    handler = ContractHandler(orm)
    contract = handler.retrieve_contract(1)
    orm.get_contract.assert_called_once_with(1)
    print(contract)
    assert contract == contract_fixture


@pytest.mark.asyncio
async def test_async_create_contract(contract_fixture):
    orm = AsyncMock()
    orm.insert_contract = AsyncMock()
    orm.insert_contract.return_value = True
    handler = AsyncContractHandler(orm)
    await handler.create_contract(contract_fixture)
    orm.insert_contract.assert_called_once_with(contract_fixture)


@pytest.mark.asyncio
async def test_async_retrieve_contract(contract_fixture):
    orm = AsyncMock()
    orm.get_contract = AsyncMock()
    orm.get_contract.return_value = contract_fixture
    handler = AsyncContractHandler(orm)
    contract = await handler.retrieve_contract(1)
    orm.get_contract.assert_called_once_with(1)
    assert contract == contract_fixture


@pytest.mark.asyncio
@patch("httpx.AsyncClient.post", new_callable=AsyncMock)
async def test_verify_contract(mock_post, contract_fixture):
    orm = AsyncMock()
    orm.get_contract = AsyncMock(return_value=contract_fixture)
    handler = AsyncContractHandler(orm)
    mock_post.return_value = httpx.Response(status_code=200)
    result = await handler.verify_contract(1)
    assert result
    mock_post.assert_called_once_with(
        f"https://someapi.com/verify/{contract_fixture.contract_id}",
        content=contract_fixture.model_dump()
    )
