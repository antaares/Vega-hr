from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


async def get_markup_default(language,btn_txt):
    markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    text = btn_txt[language]
    for btn_text in text:
        button=KeyboardButton(text=btn_text)
        markup.insert(button)
    return markup


async def get_markup_default_phone(language,btn_txt):
    markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    text = btn_txt[language]
    for btn_text in text:
            button=KeyboardButton(text=btn_text,request_contact=True)
            markup.insert(button)
    return markup


async def get_markup_default_phone_again(language,btn_txt):
    markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    text = btn_txt[language]
    for index,btn_text in enumerate(text):
        if index == 0:
            button=KeyboardButton(text=btn_text,request_contact=True)
            markup.insert(button)
        else:
            markup.add(KeyboardButton(text=btn_text))
    return markup

async def get_markup_default_main(language,btn_txt):
    markup = ReplyKeyboardMarkup(row_width=3,resize_keyboard=True)
    text = btn_txt[language]
    for index,btn_text in enumerate(text):
        button=KeyboardButton(text=btn_text)
        if index>5 and index<8:
            markup.insert(button)
        else:
            markup.add(button)
    return markup


async def get_markup_default_ads(language,btn_txt,back_btn):
    markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    text = btn_txt[language]
    for btn_text in text:
        button=KeyboardButton(text=btn_text)
        markup.insert(button)
    for btn in back_btn[language]:
        markup.add(KeyboardButton(text=btn))
    return markup

async def get_markup_defaul_admin_ads(language,btn_txt):
    markup = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    text = btn_txt[language]
    for index,btn_text in enumerate(text):
        button=KeyboardButton(text=btn_text)
        if index>4 :
            markup.add(button)
        else:
            markup.insert(button)
    return markup