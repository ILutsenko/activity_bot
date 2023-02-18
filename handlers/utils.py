from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from database.fsm_machines import FSMAdmin
from handlers.client import (
    start_handler,
)
from handlers.task_handlers import (
    answer,
    cancel,
    create_new_task,
    create_task,
    tasks,
)


def register_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(tasks, commands=['Задачи'])
    dp.register_callback_query_handler(answer)
    dp.register_message_handler(
        create_task,
        commands=['Создать_задачу'],
        state=None,
    )
    dp.register_message_handler(cancel, state='*', commands='отмена')
    dp.register_message_handler(
        cancel,
        Text(equals='отмена', ignore_case=True),
        state='*',
    )
    dp.register_message_handler(create_new_task, state=FSMAdmin.task_name)
    dp.register_message_handler(start_handler, commands=['start', 'help'])
