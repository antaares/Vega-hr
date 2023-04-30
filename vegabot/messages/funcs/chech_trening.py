from loader import db

async def check_user_db(telegram_id,tree_id):
    tree = []
    user_tree_id = await db.select_all_trening(telegram_id)
    for id in user_tree_id:
        if tree_id==id[2]:
            tree.append(id[2])
        else:
            continue
    if tree:
        return False
    else:
        return True
