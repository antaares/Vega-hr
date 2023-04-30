from aiogram.types import *
from datetime import date,datetime, timedelta
from data.config import ADMINS
from loader import dp, db
from messages.funcs.get_language import get_language
from messages.message_txt.message_text import *



@dp.message_handler(commands=['admin'],user_id=ADMINS[0], state='*')
async def get_admin(message: Message):
    language = await get_language(user_id=message.from_user.id)
    jobs_list = []
    dayyy = datetime.now()-timedelta(7)
    count = await db.count_users()
    userssss = await db.select_7den(dayyy,datetime.now())
    for i in range(len(userssss)):
        jobs_list.append(userssss[i][13])
    await message.answer(
            activ_users_vacan[language].format(str(dayyy).split('.')[0], str(datetime.now()).split('.')[0], ";\n".join(set(jobs_list)),
                                               len(jobs_list)))

    await message.answer(count_users[language].format(count))

    jobs_list.clear()

    # for i in range(len(users)):
    #     if users[i][13] != None:
    #         jobs_list.append(users[i][13])
    #
    #     if users[i][13] in ["O'quv ishlari bo'yicha mutaxassis (Metodist)","Педагог (методист)"]:
    #         jobs_list_all.append('a')
    #     elif users[i][13] in ["Bog'cha tarbiyachisi","Воспитатель детского сада"]:
    #         jobs_list_all.append('b')
    #     elif users[i][13] in ["Boshlangich o'qituvchisi","Воспитатель начальных классов"]:
    #         jobs_list_all.append('c')
    #     elif users[i][13] in ["Rus tili o'qituvchisi","Учитель русского языка"]:
    #         jobs_list_all.append('d')
    #     elif users[i][13] in ["Ingiliz tili o'qituvchisi","Учитель английского языка"]:
    #         jobs_list_all.append('e')
    #     elif users[i][13] in ["Mental arifmetika o'qituvchisi","Учитель ментальной арифметики"]:
    #         jobs_list_all.append('f')
    #     elif users[i][13] in ["Arab tili o'qituvchisi","Учитель арабского языка"]:
    #         jobs_list_all.append('j')
    #     elif users[i][13] in ["Hamshira","Медсестра"]:
    #         jobs_list_all.append('k')
    #     elif users[i][13] in ["Administrator(reception)","Администратор (приемная)"]:
    #         jobs_list_all.append('l')
    #     elif users[i][13] in ["HR(Hodimlar bo'limi)","HR (отдел кадров)"]:
    #         jobs_list_all.append('m')
    #     elif users[i][13] in ["Xo'jalik ishlari xodimi(erkak kishi kerak)","Домработница (требуется мужчина)"]:
    #         jobs_list_all.append('n')
    #     elif users[i][13] in ["Oshpaz, Oshpaz yordamchisi","Повар, Помощник повара"]:
    #         jobs_list_all.append('o')
    #     elif users[i][13] in ["Bog'bon qo'riqchi","Садовник-охранник"]:
    #         jobs_list_all.append('p')
    #     elif users[i][13] in ["Elektrik, texnik","Электрик, Техник"]:
    #         jobs_list_all.append('q')
    #     elif users[i][13] in ["Shofyor","Водитель"]:
    #         jobs_list_all.append('r')
    #     elif users[i][13] in ["Loyihada ish yurituvchi, boshqaruvchi","Менеджер проектов, Управляющий делами"]:
    #         jobs_list_all.append('s')
    # counts.append(jobs_list_all.count('a'))
    # counts.append(jobs_list_all.count('b'))
    # counts.append(jobs_list_all.count('c'))
    # counts.append(jobs_list_all.count('d'))
    # counts.append(jobs_list_all.count('e'))
    # counts.append(jobs_list_all.count('f'))
    # counts.append(jobs_list_all.count('g'))
    # counts.append(jobs_list_all.count('h'))
    # counts.append(jobs_list_all.count('i'))
    # counts.append(jobs_list_all.count('j'))
    # counts.append(jobs_list_all.count('k'))
    # counts.append(jobs_list_all.count('l'))
    # counts.append(jobs_list_all.count('m'))
    # counts.append(jobs_list_all.count('n'))
    # counts.append(jobs_list_all.count('o'))
    # counts.append(jobs_list_all.count('p'))
    # counts.append(jobs_list_all.count('q'))
    # counts.append(jobs_list_all.count('r'))
    # counts.append(jobs_list_all.count('s'))
    # for j in range(len(date_list)):
    #     if int(date_list[j].split('-')[2]) >= dayyy.day and int(date_list[j].split('-')[2]) <= date.today().day:
    #         sorted_list.append(await db.select_user(day=date_list[j]))
    #
    # for i in range(len(sorted_list)):
    #     sorted_list2.append(sorted_list[i][13])
    # await message.answer(activ_users_vacan[language].format(date.today()-timedelta(7),date.today(),";\n".join(set(sorted_list2)),len(sorted_list)))
    # print(sorted_list2)
    # print(sorted_list)
    # jobs_list_all.clear()
    # jobs_list.clear()
    # counts.clear()
    # date_list.clear()
    # sorted_list.clear()
    # sorted_list2.clear()
    #
