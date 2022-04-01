import logging
from token_pass import TOCKEN_TEST_BOT
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = TOCKEN_TEST_BOT

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        '''
        # Old fashioned way:
        await bot.send_photo(
            message.chat.id,
            photo,
            caption='Cats are here 😺',
            reply_to_message_id=message.message_id,
        )
        '''

        await message.reply_photo(photo, caption='Cats are here 😺')


from aiogram.types import ContentType

# @dp.message_handler(content_types=ContentType.ANY)
@dp.message_handler(content_types=ContentType.LEFT_CHAT_MEMBER)
async def echo(message: types.Message):
    chat_del = message.chat.title
    text = "Delete chat:" + chat_del
    print(text)
    await bot.send_message(chat_id=545960544, text=text)
    # await message.copy_to(message.chat.id)

from aiogram.types import ChatType

# @dp.message_handler(chat_type=[ChatType.PRIVATE, ChatType.SUPERGROUP])
@dp.message_handler(chat_type=[ChatType.SUPERGROUP])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends message in private chat
    """
    await message.reply("Hi!\nI'm hearing your messages only in private chats")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
