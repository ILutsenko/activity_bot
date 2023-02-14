from aiogram.utils import executor

from app import (
    db_executor,
    dispatcher,
    notice_checker,
)
from handlers.utils import register_handlers


if __name__ == '__main__':
    register_handlers(dispatcher)
    db_executor.init_database()
    dispatcher.loop.create_task(notice_checker.run_notification_handler())
    executor.start_polling(dispatcher=dispatcher)
