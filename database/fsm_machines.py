from aiogram.dispatcher.filters.state import (
    State,
    StatesGroup,
)


class FSMAdmin(StatesGroup):
    task_name = State()
