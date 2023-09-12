from aiogram import Bot, Dispatcher
import asyncio
import logging
from core.settings import TOKEN, ADMIN_ID


async def start_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущен')


async def start():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
