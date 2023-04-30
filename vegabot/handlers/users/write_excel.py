# from openpyxl import load_workbook
# import os
# from loader import db,dp
# from data.config import ADMINS
# from aiogram.types import *
# from messages.funcs.get_language import get_language
# from messages.message_txt.message_text import count_users
#
#
# @dp.message_handler(commands=['all_users'], user_id=ADMINS[0])
# async def get_users(message: Message):
#     users = await db.select_all_users()
#     count = await db.count_users()
#     language = await get_language(message.from_user.id)
#     await message.answer(count_users[language].format(count))
#
#     def make_excel(users):
#         wb = load_workbook('data/SampleData.xlsx')
#         ws = wb.active
#         c = 2
#         for u in users:
#             c += 1
#             ws[f'A{c}'] = u[3]
#             ws[f'B{c}'] = u[4]
#             ws[f'C{c}'] = u[5]
#
#         wb.save('data/UserInfo.xlsx')
#
#     make_excel(users)
#     try:
#         await message.answer_document(document=InputFile(path_or_bytesio='data/UserInfo.xlsx'))
#     except Exception as e:
#         print(e)
#     os.remove('data/UserInfo.xlsx')
#
