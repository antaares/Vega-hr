from loader import db


async def check_user(user_id):
    if await db.select_user(telegram_id=int(user_id)) == None:
        return False
    else:
        return True
