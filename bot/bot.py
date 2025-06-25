import asyncio
from aiogram import Bot, Dispatcher
from config import API_TOKEN
from handlers import all_routers


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher()

    for router in all_routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())