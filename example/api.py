from pydantic import BaseModel, Field, ConfigDict
from typing import Union

from fastapi import FastAPI, Query, Body

app = FastAPI()


class TestBodyObject(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    item_name: str = Field(alias="itemName", description="Item Name Description")


@app.get("/")
def read_root(test_query_item: str = Query("default value", alias="testQueryItem", description="Query Item Description")):
    return {"test_query_item": test_query_item}


@app.post("/", response_model=TestBodyObject)
def post_root(test_body_item: TestBodyObject = Body(alias="testBodyItem", description="Body Item Description")):
    return test_body_item
