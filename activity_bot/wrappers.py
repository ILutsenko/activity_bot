import logging
from datetime import datetime

from aiogram.types import Message

from activity_bot.models import MessageModel

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def handler_logging(func):
    def wrapper(message: Message, *args, **kwargs):
        model = MessageModel.parse_obj(dict(message.from_user))
        logger.info(f'{model.user_id}: {model.full_name} ---{datetime.now()}')
        func(message)
    return wrapper
