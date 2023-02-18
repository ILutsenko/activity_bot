from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.types.web_app_info import WebAppInfo

web_app = WebAppInfo(url="https://ilutsenko.github.io/activity_bot/")
tasks_button = InlineKeyboardButton('/Задачи', callback_data='www')
create_task_button = InlineKeyboardButton('/Создать_задачу', callback_data='www')
one_butt = InlineKeyboardButton(text="Веб версия приложения", web_app=web_app)

row = [tasks_button, create_task_button]


tasks_group = InlineKeyboardMarkup(resize_keyboard=True)
tasks_group.row(*row).add(one_butt)

__all__ = (
    'tasks_group',
)
