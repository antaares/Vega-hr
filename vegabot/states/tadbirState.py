from aiogram.dispatcher.filters.state import State,StatesGroup

class TreningState(StatesGroup):
    band = State()
    type_price = State()
    comfirm_price = State()
    send_invoice = State()


class TreningDeleteState(StatesGroup):
    delete = State()
