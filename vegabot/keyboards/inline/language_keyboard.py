from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language_keyboard = InlineKeyboardMarkup(row_width=2)
language_keyboard.add(InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="uz"))
language_keyboard.add(InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru"))
