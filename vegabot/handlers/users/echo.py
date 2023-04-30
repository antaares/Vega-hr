from aiogram import types

from loader import dp, db


from data.config import ADMINS



# Echo bot
@dp.message_handler(commands='drop',state="*",chat_type='private')
async def bot_echo(message: types.Message):
    if message.from_user.id in ADMINS:
        await db.drop_users()
        await message.answer('Dropped')

