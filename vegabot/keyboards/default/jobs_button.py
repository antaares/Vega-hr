from aiogram.types import ReplyKeyboardMarkup, KeyboardButton






async def get_jobs_button(language):
    text = {
        'vacancy1': {
            'uz': '👨‍💻 Sotuv bo\'limi',
            'ru': '👨‍💻 Отдел продаж',
        },
        'vacancy2': {
            'uz': '👨‍💼 Kassir',
            'ru': '👨‍💼 Кассир',
        }
    }
    jobs_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=text['vacancy1'][language]),
                KeyboardButton(text=text['vacancy2'][language])
            ]
        ],
        resize_keyboard=True
    )
    return jobs_btn
