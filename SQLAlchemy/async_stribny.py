from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from fastapi_asyncalchemy.db.base import Base



class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, unique=True)
    population = Column(Integer)

'''
names = ['Larry', 'Curly', 'Moe']
message = 'The Three Stooges: '
for index, name in enumerate(names):
    if index > 0:
        message += ', '
    if index == len(names) - 1:
        messaeg += 'and '
    message += name
print(message)
'''
