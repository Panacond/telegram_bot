import logging
from aiogram import Bot, Dispatcher, types, executor
from token_pass import TOCKEN_TEST_BOT
from example_chat_bot_text import Cha

API_TOKEN = TOCKEN_TEST_BOT

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bot_chat = Cha()

async def on_startup():
    user_should_be_notified = 545960544
    await bot.send_message(user_should_be_notified, "Hello, I'm bot")

@dp.message_handler(commands=['bug'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!")

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    await message.answer(bot_chat.get_response(message.text))

if __name__ == '__main__':
    executor.start(dp, on_startup())
    executor.start_polling(dp, skip_updates=True)