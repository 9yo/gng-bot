from structs.user import User

from pymongo.collection import Collection


def get_user(db: Collection, chat_id: int):
    raw_user = db.users.find_one({'chat_id': chat_id})
    if not raw_user:
        return None
    else:
        return User.from_json(raw_user)

def create_user(db: Collection, chat_id: int):
    if not get_user(db, chat_id):
        user: User = User(chat_id=chat_id)
        db.users.insert_one(user.reprJSON())
        print('created')
        return True
    return False
