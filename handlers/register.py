from aiogram import Router,F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.register import RegisterState
from keyboards.reply import start_reply

router=Router()

@router.message(F.text=="Register")
async def register(msg: Message,state: FSMContext,db):
    if await db.is_user_exists(msg.from_user.id):
        await msg.answer("Siz avval ro'yxatdan o'tgansiz! Asosiy menyudan foydalanishingiz mumkin!",reply_markup=start_reply())
    else:
        await msg.answer("Registratsiyadan o'tish uchun ismingizni kiriting!")
        await state.set_state(RegisterState.name)

@router.message(RegisterState.name)
async def register(msg: Message,state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Familiyangizni kiriting!")
    await state.set_state(RegisterState.surename)

@router.message(RegisterState.surename)
async def register(msg: Message,state: FSMContext):
    await state.update_data(surename=msg.text)
    await msg.answer("Yoshingizni kiriting!")
    await state.set_state(RegisterState.age)

@router.message(RegisterState.age)
async def register(msg: Message,state: FSMContext):
    await state.update_data(age=int(msg.text))
    await msg.answer("Telefon raqamingizni kiriting!")
    await state.set_state(RegisterState.phone_number)

@router.message(RegisterState.phone_number)
async def register(msg: Message,state: FSMContext,db):
    await state.update_data(phone_number=msg.text)

    data=await state.get_data()
    await msg.answer(text=f"Sizni ma'lumotlaringiz:\nIsmingiz: {data['name']}\nFamiliyangiz: {data['surename']}\nYoshingiz: {data['age']}\nTelefon raqamingiz: {data['phone_number']}")
    await db.add_user(int(msg.from_user.id),data["name"],data["surename"],data["age"],data["phone_number"])
    await msg.answer("Ma'lumotlaringiz muvaffaqiyatly saqlandiii!",reply_markup=start_reply())
    await state.clear()