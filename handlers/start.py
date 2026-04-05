from aiogram import Router,F
from aiogram.types import Message
from aiogram.filters import CommandStart
from filters.adminfilter import RoleFilter
from keyboards.reply import register,start_reply,start_reply_admin

router=Router()



@router.message(CommandStart(),RoleFilter('admin'))
async def start_handler(msg: Message):
    await msg.answer(f"Assalomu alaykum {msg.from_user.first_name} admin botga xush kelibsiz! ",reply_markup=start_reply_admin())


@router.message(CommandStart())
async def start_handler(msg: Message,db):
    if await db.is_user_exists(msg.from_user.id):
            await msg.answer(f"Assalomu alaykum {msg.from_user.first_name} botga xush kelibsiz! Siz Ro'yxatdan o'tganinsiz!",reply_markup=start_reply())
    else:
        await msg.answer(f"Assalomu alaykum {msg.from_user.first_name} botga xush kelibsiz!\nIltimos Registratsiyadan o'ting!",reply_markup=register())