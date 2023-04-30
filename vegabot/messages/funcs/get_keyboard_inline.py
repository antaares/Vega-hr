from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



async def get_markup_inline2(language,btn_txt):
    markup = InlineKeyboardMarkup(row_width=3)
    text = btn_txt[language]
    for btn_text in text:
        button=InlineKeyboardButton(text=btn_text,callback_data=btn_text)
        markup.insert(button)
    return markup


async def get_markup_inline(language,btn_txt):
    markup = InlineKeyboardMarkup(row_width=2)
    text = btn_txt[language]
    for btn_text in text:
        button=InlineKeyboardButton(text=btn_text,callback_data=btn_text)
        markup.add(button)
    return markup

async def get_markup_inline_admin(language,btn_txt):
    markup = InlineKeyboardMarkup(row_width=1)
    text = btn_txt[language]
    for btn_text in text:
        button=InlineKeyboardButton(text=btn_text,url='t.me/JO_SHINE_admin')
        markup.add(button)
    return markup

async def get_markup_inline_insert(language,btn_txt):
    markup = InlineKeyboardMarkup(row_width=2)
    text = btn_txt[language]
    for btn_text in text:
        button=InlineKeyboardButton(text=btn_text,callback_data=btn_text)
        markup.insert(button)
    return markup



async def get_answer_btn(user_id, language, btn_txt):
    markup = InlineKeyboardMarkup(row_width=1)
    text = btn_txt[language]
    for btn_text in text:
        button = InlineKeyboardButton(text=btn_text, callback_data=f'{btn_text}_{user_id}')
        markup.add(button)
    return markup



async def get_markup_inline_insert_index(language,btn_txt,user_id,trening_id):
    markup = InlineKeyboardMarkup(row_width=2)
    text = btn_txt[language]
    for btn_text in text:
        button=InlineKeyboardButton(text=btn_text,callback_data=f"{btn_text}_{user_id}_{trening_id}")
        markup.insert(button)
    return markup