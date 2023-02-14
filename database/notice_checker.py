import asyncio
import logging
from datetime import (
    datetime,
    timedelta,
)

from typing import TYPE_CHECKING

from activity_bot.constants import TaskStatus

if TYPE_CHECKING:
    from database.db_executor import DatabaseExecutor
    from aiogram import Bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class NoticeChecker:
    def __init__(self, db_executor: 'DatabaseExecutor', bot: 'Bot'):
        self._db_executor = db_executor
        self._bot = bot
        self._last_check = None

    async def run_notification_handler(self):
        logger.info('Notification handler started.')
        if not self._last_check:
            self._last_check = datetime.now()

        while True:
            notifications = self._db_executor.get_notifications(
                status=TaskStatus.ACTIVE,
            ) or []
            for notice in notifications:
                delta = timedelta(
                    hours=notice.step.hour,
                    minutes=notice.step.minute,
                    seconds=notice.step.second,
                )
                check_time = notice.last_notice + delta
                if datetime.now() >= check_time:
                    await self._db_executor.send_notification(
                        user_id=notice.user_id,
                        task_name=notice.task_name,
                        bot=self._bot,
                    )
            await asyncio.sleep(5)
