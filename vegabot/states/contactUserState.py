from aiogram.dispatcher.filters.state import State,StatesGroup

class ContactState(StatesGroup):
    send_message = State()
    answer_admin = State()