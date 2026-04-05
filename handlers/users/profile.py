from aiogram import F,Router
from aiogram.types import Message

router=Router()

@router.message(F.text=="Profile")
async def profile(msg:Message,db):
    tg_id=msg.from_user.id
    data = await db.profile(tg_id)
    await msg.answer(f"Siznign ma'lumotlaringiz:\nIsmingiz: {data['name']}\nFamilyangiz: {data['surename']}\nYoshingiz: {data['age']}\nTelefon raqamingiz: {data['phone_number']}\nRole: {data['role']}")