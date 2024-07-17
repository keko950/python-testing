from python_testing.routes.contracts import contracts_router
from fastapi import FastAPI

app = FastAPI()

app.include_router(contracts_router)
