from aiogram import (
    Bot,
    Dispatcher,
    executor,
)
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from activity_bot.config import config
from database.sql_executor import DatabaseExecutor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import (
    StatesGroup,
    State,
)
from activity_bot.handlers import (
    tasks,
    create_task,
    create_new_task,
    start_handler,
)


class FSMAdmin(StatesGroup):
    task_name = State()


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(tasks, commands=['Задачи'])
    dp.register_message_handler(create_task, commands=['Создать_задачу'], state=None)
    dp.register_message_handler(create_new_task, state=FSMAdmin.task_name)
    dp.register_message_handler(start_handler, commands=['start', 'help'])


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
    'FSMAdmin',
    'db_executor',
    'dispatcher',
    'executor',
    'engine',
)
