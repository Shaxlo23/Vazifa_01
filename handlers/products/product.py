from aiogram import F,Router
from aiogram.types import Message
from keyboards.inline import product_inline
router=Router()

@router.message(F.text=="Bozor")
async def products(msg:Message,db):
    products= await db.get_products()
    await msg.answer(f"Bozordagi Mahsulotlar ro'yxati: ",reply_markup=product_inline(products))