from sqlalchemy import (
    BigInteger,
    Column,
    String,
    DateTime, Time,
)

from database.declarative_base import base


class NotificationTable(base):
    __tablename__ = "notifications"

    notice_id = Column(
        BigInteger,
        primary_key=True,
        nullable=False,
        autoincrement=True,
    )
    user_id = Column(BigInteger, nullable=False)
    last_notice = Column(DateTime, nullable=True)
    step = Column(Time, nullable=False)
    status = Column(String, nullable=False)
    task_name = Column(String, nullable=False)
