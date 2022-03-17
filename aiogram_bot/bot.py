#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
logging.basicConfig(level=logging.INFO)

bot = Bot(token="1426091599:AAH0FiP0WvsVXCJ74FKpQTUMrp87bzuZcck")
'''только для pycharm при задании переменных окружения'''
# bot_token = getenv("BOT_TOKEN")
# if not bot_token:
#     exit("Error: no token provided")

# bot = Bot(token=bot_token)

dp = Dispatcher(bot)

# возвращать сообщения на сообщения
@dp.message_handler()
async def echo(message: types.Message):
    if "1" in message.text:
        await message.reply(message.text)
    if "hi" in message.text:
        sender = "Это ваш ответ?:" + message.text
        await bot.send_message(chat_id=-702529372, text=sender)
        # await message.answer( text=sender)

# чтоб событие работало
dp.register_message_handler(echo)




# возвращать сообщения на сообщения
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     if "hi" in message.text:
#         sender = "Это ваш ответ?:" + message.text
#         await message.answer(sender)

# чтоб событие работало
# dp.register_message_handler(echo_message)

# пишешь в бота он в группу кидает этодзи
# @dp.message_handler(commands="dice")
# async def cmd_dice(message: types.Message):
#     await message.bot.send_dice(-702529372, emoji="🎲")

# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")

# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.answer("Test 2")

dp.register_message_handler(cmd_test2, commands="test2")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)