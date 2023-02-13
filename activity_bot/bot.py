from aiogram.utils import executor

from app import (
    db_executor,
    dispatcher,
)
from handlers.utils import register_handlers

if __name__ == '__main__':
    register_handlers(dispatcher)
    db_executor.init_database()
    executor.start_polling(dispatcher=dispatcher)
