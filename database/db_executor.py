import datetime
import logging

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker

from activity_bot.constants import TaskStatus
from database.declarative_base import base
from database.tables import (
    NotificationTable,
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
        return session.query(TaskTable).filter(
            TaskTable.user_id == user_id
        ).all()

    def create_task(
            self,
            user_id: int,
            task_name: str,
            step: datetime.time = datetime.time(second=5),
    ):
        session = self._get_session()()
        task_query = TaskTable(
            user_id=user_id,
            task_name=task_name,
            status=TaskStatus.OPEN,
        )
        notice_query = NotificationTable(
            user_id=user_id,
            last_notice=datetime.datetime.now(),
            step=step,
            status=TaskStatus.OPEN,
            task_name=task_name,
        )
        session.add_all([task_query, notice_query])
        session.commit()

    def get_notifications(self, status: str):
        session = self._get_session()()
        return session.query(NotificationTable).\
            filter(NotificationTable.status == status).\
            order_by(NotificationTable.last_notice).all()

    async def send_notification(self, user_id: int, task_name: str, bot):
        session = self._get_session()()
        notice = session.query(NotificationTable).filter(
            NotificationTable.status == TaskStatus.ACTIVE,
            NotificationTable.task_name == task_name,
        ).one()
        notice.last_notice = datetime.datetime.now()
        session.add(notice)
        session.commit()
        await bot.send_message(
            user_id,
            f'---Напоминание---\nНеобходимо выполнить задачу: {task_name}!\n'
            f'Следующее напоминание будет через {notice.step}',
        )
