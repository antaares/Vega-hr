from datetime import datetime

import pytz
from aiogram import types

from loader import db

tz = pytz.timezone('Asia/Tashkent')


async def sort(type):
    arrYMD = []
    arrYDM = []
    trening = await db.select_all_online(type)

    now = datetime.now()
    if trening:
        for i in range(len(trening)):
            arrYMD.append(datetime.strptime(f"{trening[i][8].strip()}", "%d.%m.%Y %H:%M"))

        for j in range(len(arrYMD)):
            if arrYMD[j] >= now:
                arrYDM.append(arrYMD[j])
            else:
                id = trening[j][0]
                await db.update_admin_holat(holat=False, id=int(id))
                await db.delete_tadbir_tree(trening_id=int(id))

        return sorted(arrYDM)
    else:
        pass

async def sort_free(type):
    arrYMD = []
    arrYDM = []
    trening = await db.select_all_freee(type)
    now = datetime.now()
    if trening:
        for i in range(len(trening)):
            arrYMD.append(datetime.strptime(f"{trening[i][8].strip()}", "%d.%m.%Y %H:%M"))

        for j in range(len(arrYMD)):
            if arrYMD[j] >= now:
                arrYDM.append(arrYMD[j])
            else:
                id = trening[j][0]
                await db.update_admin_holat(holat=False, id=int(id))
                await db.delete_tadbir_tree(trening_id=int(id))
        return sorted(arrYDM)
    else:
        pass

async def pagination(page: int=1, trening=None, user_id=None):
    limit = 5
    menus = [f"{trening[i][5]}" for i in range(len(trening))]
    markup = types.InlineKeyboardMarkup(row_width=1)
    offset = limit * (page-1)
    for index, i in enumerate(menus[offset:page*limit]): # menus[0:4]
        markup.add(
            types.InlineKeyboardButton(i, callback_data=f"menu_{trening[index][0]}")
        )

    markup.row(types.InlineKeyboardButton(text="🔙 Orqaga",callback_data=f'backeee_{user_id}'))
    return markup


async def pagination2(page: int=1, trening=None, user_id=None):
    limit = 5
    menus = [f"{trening[i][5]}" for i in range(len(trening))]
    markup = types.InlineKeyboardMarkup(row_width=1)
    offset = limit * (page-1)
    for index, i in enumerate(menus[offset:page*limit]): # menus[0:4]
        markup.add(
            types.InlineKeyboardButton(i, callback_data=f"uneeess_{trening[index][0]}")
        )

    markup.row(types.InlineKeyboardButton(text="🔙 Orqaga",callback_data=f'backee_{user_id}'))
    return markup
