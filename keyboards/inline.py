from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def users_inline(users):
    keyboards=[]

    for user in users:
        keyboards.append([InlineKeyboardButton(text=f"{user['name']} {user['surename']}({user['role']})",callback_data=f"user_{user['id']}")])


    return  InlineKeyboardMarkup(inline_keyboard=keyboards)

def user_action(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="admin",callback_data=f"changeto_admin_{user_id}"),InlineKeyboardButton(text="user",callback_data=f"changeto_user_{user_id}")]
        ]

    )