import asyncio
import aioschedule
import logging
from aiogram import Bot, Dispatcher, executor


# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = "BOT:TOKEN"

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    asyncio.create_task(scheduler())
    text = "I'm work now"
    user_should_be_notified = -702529372
    await bot.send_message(user_should_be_notified, text)


async def noon_print():
    text = "I'm work"
    print(text)
    user_should_be_notified = -702529372
    await bot.send_message(user_should_be_notified, text)

async def scheduler():
    aioschedule.every().day.at("6:00").do(noon_print)
    aioschedule.every(1).minutes.do(noon_print)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)