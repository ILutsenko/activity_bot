from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
)

tasks_button = KeyboardButton('/Задачи')
create_task_button = KeyboardButton('/Создать_задачу')

tasks_group = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tasks_group.add(tasks_button)
tasks_group.add(create_task_button)

__all__ = (
    'tasks_group',
)
