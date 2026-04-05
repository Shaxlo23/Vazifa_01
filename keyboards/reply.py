from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def register():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Register")]
        ],
        resize_keyboard=True
    )


def start_reply():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bozor"),KeyboardButton(text="Mening Buyurtmalarim")],
            [KeyboardButton(text="Profile"),KeyboardButton(text="Savatcha")]
        ],
        resize_keyboard=True
    )

def start_reply_admin():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bozor"),KeyboardButton(text="Mening buyurtmalarim")],
            [KeyboardButton(text="Profile"),KeyboardButton(text="Admin panel")]
        ],
        resize_keyboard=True
    )


def admin_panel():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Bozorga mahsulotlar qo'shish"),KeyboardButton(text="Mahsulotlarni yangilash")],
            [KeyboardButton(text="Users"),KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )