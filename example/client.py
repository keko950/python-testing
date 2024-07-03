from api import TestBodyObject
import requests

r = requests.get('http://localhost:8000')
print(r.json())


object = TestBodyObject(item_name="item_name")
r = requests.post('http://localhost:8000',
                  json=object.model_dump())
print(r.json())
