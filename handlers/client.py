import logging
from datetime import datetime

from aiogram.types import Message

from activity_bot.keyboards import tasks_group
from app import bot

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start_handler(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    logger.info(f'---{datetime.now()}--- {user_id}: {user_name}')

    await message.reply(f'{user_name}, ДОРОУ!')
    await bot.send_message(user_id, text='Выбери кнопку в меню', reply_markup=tasks_group)
