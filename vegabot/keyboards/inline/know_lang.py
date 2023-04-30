from aiogram import types
from messages.btn_text.btn_text import know_lang_txt_btn

async def get_markup(data):
    markup = types.InlineKeyboardMarkup(row_width=2)
    for index, value in enumerate(data):
        if index < 5:
            markup.insert(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))
        else:
            markup.row(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))
    return markup

async def get_kb(data,language):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if data.split('_')[0] in know_lang_txt_btn[language]:
        if data.split('_')[0].startswith('✅'):
            i = int(know_lang_txt_btn[language].index(data.split('_')[0]))
            know_lang_txt_btn[language].pop(i)
            know_lang_txt_btn[language].insert(i,f"{(data.split('_')[0]).split('✅')[1].lstrip()}")

            for index, value in enumerate(know_lang_txt_btn[language]):
                if index < 5:
                    markup.insert(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))
                else:
                    markup.row(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))
        else:
            i = int(know_lang_txt_btn[language].index(data.split('_')[0]))
            know_lang_txt_btn[language].pop(i)
            know_lang_txt_btn[language].insert(i, f"✅ {data.split('_')[0]}")

            for index, value in enumerate(know_lang_txt_btn[language]):
                if index < 5:
                    markup.insert(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))
                else:
                    markup.row(types.InlineKeyboardButton(text=value, callback_data=f"{value}_{index}"))

    return markup

