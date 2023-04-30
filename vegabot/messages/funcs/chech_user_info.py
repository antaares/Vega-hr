from loader import db


async def check_user_info(args,user_id,lang):
    user_dick = {
        '❗ ':'Ko\'rsatilmagan'
    }
    user_dick_ru = {
        '❗ ': 'Кўрсатилмаган'
    }
    user=await db.select_user(telegram_id=int(user_id))
    if lang=='uz':
        if user.get(f'{args}'):
            return {'✅ ': user.get(f'{args}')}
        else:
            return user_dick

    else:
        if user.get(f'{args}'):
            return {'✅ ': user.get(f'{args}')}
        else:
            return user_dick_ru


