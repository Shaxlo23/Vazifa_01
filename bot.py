from aiogram import Bot,Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

from config import config

from handlers.start import router as start_router

async def main():
    bot=Bot(token=config.BOT_TOKEN)
    dp=Dispatcher(storage=MemoryStorage())

    dp.include_router(start_router)

    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())