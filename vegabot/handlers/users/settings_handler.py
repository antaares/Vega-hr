from aiogram import types

from keyboards.inline.language_keyboard import language_keyboard
from loader import dp, db
from messages.funcs.check_user import check_user
from messages.funcs.get_language import get_language
from messages.message_txt.message_text import *


@dp.message_handler(text=["🇺🇿 Tilni o'zgartirish","🇷🇺 Изменить язык"])
async def reg_to_bot(message: types.Message):
    if await check_user(user_id=message.from_user.id) == False:
        await db.add_user(telegram_id=message.from_user.id,
                          language='uz',
                          fullname=None,
                          date=None,
                          day=None,
                          phone=None,
                          addphone=None,
                          malumot=None,
                          manzil=None,
                          oilaviy_holat=None,
                          sud_holat=None,
                          company=None,
                          new_company=None,
                          last_summa=None,new_summa=None,time_job=None, know_lang=None,know_lang_degree=None,
                          abaut_as=None)
    language = await get_language(user_id=message.from_user.id)
    if language is None:
        language = "uz"
    await message.answer(change_language_txt[language],
                         reply_markup= language_keyboard)




