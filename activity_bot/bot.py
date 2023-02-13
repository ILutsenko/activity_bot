import logging

from app import (
    dispatcher,
    executor,
    db_executor,
    register_handlers,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    register_handlers(dispatcher)
    db_executor.init_database()
    executor.start_polling(dispatcher=dispatcher)
