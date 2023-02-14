from asyncio import get_event_loop

from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from activity_bot.config import config
from database.db_executor import DatabaseExecutor
from database.notice_checker import NoticeChecker

url = URL.create(
    drivername='postgresql',
    username=config.database.username,
    password=config.database.password,
    host=config.database.host,
    port=config.database.port,
    database=config.database.database,
)

engine = create_engine(url)

bot = Bot(token=config.telegram_settings.token)
dispatcher = Dispatcher(bot=bot, storage=MemoryStorage(), loop=get_event_loop())

db_executor = DatabaseExecutor(engine=engine)

notice_checker = NoticeChecker(db_executor=db_executor, bot=bot)


__all__ = (
    'bot',
    'db_executor',
    'notice_checker',
    'dispatcher',
    'engine',
)
