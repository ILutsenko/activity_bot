from sqlalchemy import (
    Column,
    BigInteger,
    String,
)

from database import base


class UserTable(base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
