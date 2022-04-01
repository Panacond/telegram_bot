# for library aiogram 3.0

from distutils.log import error
import logging
from typing import Any

from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.methods import SendMessage
from token_pass import TOCKEN_TEST_BOT

TOKEN = TOCKEN_TEST_BOT
dp = Dispatcher()

logger = logging.getLogger(__name__)

@dp.message(commands=["start"])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most of event objects has an aliases for API methods to be called in event context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage` method automatically
    # or call API method directly via Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@dp.message()
async def message_handler(message: types.Message):
    
    # print(text)
    # await message.answer(text)
    # await SendMessage(message.chat.id, message.text)
    try:
        text = message.text
        await SendMessage(chat_id=545960544, text=text)
    except:
        text = "test_work_bot left the chat: "+  message.chat.title
        await SendMessage(chat_id=545960544, text=text)
# @dp.channel_post()
# async def her(channel_post: types.Message) -> Any:
#     print(channel_post.text)
#     await channel_post.answer(channel_post.text)
# async def message_handler(message: types.Message) -> None:
#     await message.answer("Nice try!")

# @dp.message()
# async def echo_handler(message: types.Message) -> None:
#     """
#     Handler will forward received message back to the sender

#     By default message handler will handle all message types (like text, photo, sticker and etc.)
#     """
#     try:
#         # Send copy of the received message
#         await message.send_copy(chat_id=message.chat.id)
#         await message.answer("Nice try!")
#     except TypeError:
#         # But not all the types is supported to be copied so need to handle it
#         await message.answer("Nice try!")


def main() -> None:
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode="HTML")
    # bot = Bot(TOKEN="1474991874:AAHr9frYUjJ95MJ3_mE5xuNDXvnvr3OvkFE")
    # And the run events dispatching
    dp.run_polling(bot)


if __name__ == "__main__":
    main()