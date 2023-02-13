from sqlalchemy import (
    BigInteger,
    Column,
    String,
)

from database.declarative_base import base


class UserTable(base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
