import asyncio
from aiogram import Bot, Dispatcher

from config import TOKEN
from rl import rl

dp = Dispatcher()

async def main():
    for router in rl:
        dp.include_router(router)
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())