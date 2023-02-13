from aiogram import (
    Bot,
    Dispatcher,
)
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from activity_bot.config import config
from database.db_executor import DatabaseExecutor

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
dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())

db_executor = DatabaseExecutor(engine=engine)


__all__ = (
    'bot',
    'db_executor',
    'dispatcher',
    'engine',
)
