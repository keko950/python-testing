from unittest.mock import Mock, patch, AsyncMock
from unittest import TestCase, IsolatedAsyncioTestCase
from datetime import datetime
from app.src.controllers.contract import ContractHandler
from app.src.controllers.async_contract import AsyncContractHandler
from app.src.models.contract import Contract, ContractType
import httpx


class ControllerTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("called before each test class")
        cls.contract_fixture = Contract(
            contract_id=1, name="my contract", contract_type=ContractType.CN,
            contract_start_date=datetime.utcnow(),
            shell_entity="SHELL", numberOfCargoes=20, contract_owner="gibe", created_by="gibe",
            contract_holder="SHELL", parent_contract_nickname="test", counter_party=None,
            execution_date=None)
        return super().setUpClass()

    def setUp(self) -> None:
        print("called before each test function")
        return super().setUp()

    def test_create_contract(self):
        orm = Mock()
        orm.insert_contract = Mock()
        orm.insert_contract.return_value = True
        handler = ContractHandler(orm)
        handler.create_contract(self.contract_fixture)
        orm.insert_contract.assert_called_once_with(self.contract_fixture)

    def test_retrieve_contract(self):
        orm = Mock()
        orm.get_contract = Mock()
        orm.get_contract.return_value = self.contract_fixture
        handler = ContractHandler(orm)
        contract = handler.retrieve_contract(1)
        orm.get_contract.assert_called_once_with(1)
        self.assertEqual(contract, self.contract_fixture)


class AsyncControllerTests(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("called before each test class async")
        cls.contract_fixture = Contract(
            contract_id=1, name="my contract", contract_type=ContractType.CN,
            contract_start_date=datetime.utcnow(),
            shell_entity="SHELL", numberOfCargoes=20, contract_owner="gibe", created_by="gibe",
            contract_holder="SHELL", parent_contract_nickname="test", counter_party=None,
            execution_date=None)
        return super().setUpClass()

    async def asyncSetUp(self) -> None:
        print("called before each test function async")
        return await super().asyncSetUp()

    async def test_create_contract(self):
        orm = Mock()
        orm.insert_contract = AsyncMock()
        orm.insert_contract.return_value = True
        handler = AsyncContractHandler(orm)
        await handler.create_contract(self.contract_fixture)
        orm.insert_contract.assert_called_once_with(self.contract_fixture)

    async def test_retrieve_contract(self):
        orm = Mock()
        orm.get_contract = AsyncMock()
        orm.get_contract.return_value = self.contract_fixture
        handler = AsyncContractHandler(orm)
        contract = await handler.retrieve_contract(1)
        orm.get_contract.assert_called_once_with(1)
        self.assertEqual(contract, self.contract_fixture)

    @patch("app.src.controllers.async_contract.httpx.AsyncClient.post", new_callable=AsyncMock)
    async def test_verify_contract(self, mock_post):
        orm = AsyncMock()
        orm.get_contract = AsyncMock()
        orm.get_contract.return_value = self.contract_fixture
        handler = AsyncContractHandler(orm)

        mock_post.return_value = httpx.Response(status_code=200)
        result = await handler.verify_contract(1)

        self.assertTrue(result)
        mock_post.assert_called_once_with(
            f"https://someapi.com/verify/{self.contract_fixture.contract_id}",
            content=self.contract_fixture.model_dump()
        )
