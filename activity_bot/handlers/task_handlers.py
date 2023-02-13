import logging
from datetime import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from activity_bot.wrappers import handler_logging
from app import dispatcher, db_executor, bot, FSMAdmin

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


@handler_logging
@dispatcher.message_handler(commands=['Задачи'])
async def tasks(message: Message):
    logger.info('Вызван список задач')
    all_tasks = "\n".join([
        f'{num}) {task.task_name}'
        for num, task in enumerate(db_executor.show_all_tasks(message.from_user.id), 1)
    ])
    await bot.send_message(message.from_user.id, f'Ваш список задач: \n{all_tasks}')


@dispatcher.message_handler(commands=['Создать_задачу'], state=None)
async def create_task(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logger.info(f'---{datetime.now()}--- {user_id}: {user_name}')
    logger.info('Вызвано создание задачи')
    await FSMAdmin.task_name.set()
    await message.reply('Введи название задачи')


@dispatcher.message_handler(state=FSMAdmin.task_name)
async def create_new_task(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logger.info(f'---{datetime.now()}--- {user_id}: {user_name}')
    async with state.proxy() as data:
        db_executor.create_task(
            user_id=message.from_user.id,
            task_name=message.text,
        )
        await message.reply('Задача успешно создана')
        await state.finish()
