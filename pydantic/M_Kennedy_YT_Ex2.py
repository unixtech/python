from pydantic import BaseModel
import json
from typing import Optional


with open('data.json', 'r') as json_file:
    my_dict = json.load(json_file)

class Location(BaseModel):
    city: str
    state: str
    country: Optional[str]


class User(BaseModel):
    name: str
    location: Location = None
    bike: str
    rides: list[int] = []


u = User(**my_dict)
print(u)
