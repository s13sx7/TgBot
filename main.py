import asyncio
import logging


from aiogram import Bot, Dispatcher
from config import settings
from routers import router    
    
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    bot = Bot(token=settings.Token)
    dp = Dispatcher()
    dp.include_router(router=router)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())