from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, DateTime, String, create_engine
from datetime import datetime


Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)

    @property
    def full_name(self):
        return f'{self.first_name}, {self.last_name}'

    def __repr__(self):
        return (
            f'UserModel(id={self.id}, first_name={self.first_name})'
        )



users = [
    UserModel(first_name='Bob', last_name='Preston', birth=datetime(1989, 2, 9)),
    UserModel(first_name='Susan', last_name='Sane', birth=datetime(1988, 2, 9)),
]


session_maker = sessionmaker(bind=create_engine('sqlite:///models.db')) 


def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()


create_users()

with session_maker() as session:
    user_records = session.query(UserModel).all()
    for user in user_records:
        print(user)
