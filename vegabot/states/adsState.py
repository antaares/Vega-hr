from aiogram.dispatcher.filters.state import State,StatesGroup

class ADSState(StatesGroup):
    holat1 = State()
    holat2 = State()
    send = State()
    database = State()
    all_send = State()


class ADSState22(StatesGroup):
    holat1 = State()
    holat2 = State()
    holat11 = State()
    holat12 = State()
    send = State()
    database = State()
    all_send = State()