import logging

from aiogram.dispatcher import FSMContext
from aiogram.types import (
    Message,
    ParseMode,
)

from app import (
    bot,
    db_executor,
)
from handlers.utils import FSMAdmin

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def tasks(message: Message):
    user = message.from_user
    logger.info(f'{user.id}: {user.full_name} ---список задач')
    all_tasks = db_executor.show_all_tasks(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        f'Data:\n<pre>\n{all_tasks}\n</pre>',
        parse_mode=ParseMode.HTML,
    )


async def create_task(message: Message):
    user = message.from_user
    logger.info(f'{user.id}: {user.full_name} ---создание задачи')
    await FSMAdmin.task_name.set()
    await message.reply(
        'Введи название задачи. '
        'Если передумал создавать задачу - напиши слово "отмена"',
    )


async def create_new_task(message: Message, state: FSMContext):
    user = message.from_user
    logger.info(f'{user.id}: {user.full_name} ---Введено имя таска.')
    async with state.proxy() as data:
        db_executor.create_task(
            user_id=message.from_user.id,
            task_name=message.text,
        )
        await message.reply('Задача успешно создана')
        await state.finish()


async def cancel(message: Message, state: FSMContext):
    user = message.from_user
    logger.info(f'{user.id}: {user.full_name} ---Отмена создания таска.')
    current_state = await state.get_state()
    if not current_state:
        return
    await state.finish()
    await message.reply('Создание задачи отменено.')
