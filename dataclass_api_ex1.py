from dataclasses import dataclass
from typing import List, Literal


@dataclass
class Car:
    name: str
    wheels: int

@dataclass
class APIRequest:
    cars: List[Car]
    salad: Literal['potato', 'italian']
    version: Literal[8]



payload = APIRequest(
    cars=[Car(name= 'toy yada', wheels=4,),],
    salad= 'potato',
    version=8,
)
