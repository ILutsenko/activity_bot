import logging

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from database import base
from database.tables import (
    TaskTable,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class DatabaseExecutor:
    def __init__(self, engine: Engine):
        self._engine = engine

    def init_database(self):
        base.metadata.create_all(self._engine)

    def _get_session(self):
        return sessionmaker(bind=self._engine)

    def _execute_query(self, query):
        session = self._get_session()
        logger.info('Opening session')
        with session() as con:
            logger.info('Adding query into session: %s', query)
            result = con.add(query)
            logger.info('---Commit---')
            con.commit()
        logger.info(f'session status: {session}')
        return result

    def show_all_tasks(self, user_id: int):
        session = self._get_session()()
        return session.query(TaskTable).filter(TaskTable.user_id == user_id).all()

    def create_task(self, user_id: int, task_name: str):
        query = TaskTable(user_id=user_id, task_name=task_name, status='open')
        self._execute_query(query)
