import logging

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from database.declarative_base import base
from database.tables import (
    TaskTable,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class DatabaseExecutor:
    def __init__(self, engine: Engine):
        self._engine = engine

    def init_database(self):
        base.metadata.create_all(self._engine)

    def _get_session(self):
        return sessionmaker(bind=self._engine)

    def show_all_tasks(self, user_id: int):
        session = self._get_session()()
        return session.query(TaskTable).filter(TaskTable.user_id == user_id).all()

    def create_task(self, user_id: int, task_name: str):
        session = self._get_session()()
        query = TaskTable(user_id=user_id, task_name=task_name, status='open')
        session.add(query)
        session.commit()
