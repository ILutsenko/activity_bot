from sqlalchemy import (
    BigInteger,
    Column,
    String,
)

from database.declarative_base import base


class TaskTable(base):
    __tablename__ = "task"

    task_id = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, nullable=False)
    task_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
