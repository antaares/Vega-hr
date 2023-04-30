from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.language_keyboard import language_keyboard
from loader import dp, db, bot
from messages.btn_text.btn_text import *
from messages.funcs.check_user import check_user
from messages.funcs.get_keyboard_default import get_markup_default
from messages.funcs.get_language import get_language
from messages.message_txt.message_text import *


@dp.message_handler(CommandStart(),chat_type='private',state='*')
async def bot_start(message: types.Message,state: FSMContext):
    await state.finish()
    if await check_user(user_id=message.from_user.id):
        language = await get_language(user_id=message.from_user.id)
        if language=='None':
            await message.answer(
                text=welcome_txt,
                reply_markup=language_keyboard
            )
        else:
            await message.answer(reg_bot[language],reply_markup=await get_markup_default(language, reg_btn_txt))

    else:
        await db.add_user(telegram_id=message.from_user.id,
                          language=None,
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

        await message.answer(
            text=welcome_txt,
            reply_markup=language_keyboard
        )

@dp.callback_query_handler(lambda call: call.data == "ru" or call.data == "uz")
async def language_query_handler(callback_query: types.CallbackQuery):
    await bot.delete_message(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id
    )

    await db.update_user_language(language=callback_query.data, telegram_id=callback_query.from_user.id)
    await callback_query.message.answer(main_menu_txt[callback_query.data],
                             reply_markup=await get_markup_default(callback_query.data, reg_btn_txt))


