import logging, random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parse_site import weather_sinoptic


API_TOKEN = 'BOT_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

buttons = ["weather", "Game", 'game']

async def on_startup():
    user_should_be_chat = -702529372
    user_should_be_user = 545960544
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await bot.send_message(user_should_be_user, "Бот запущен", reply_markup=keyboard)
    await bot.send_message(user_should_be_chat, "Бот ура!")


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*buttons)
    await message.reply("Hi!\nI'm Bot!\nI'm type some statements\nYou type words: мысль, идея, thought, idea, cat", reply_markup=keyboard)

text_all_time=('пес', 'dog')
STATEMENTS= (
    'Человеческий мозг – великолепная штука. Он работает до той самой минуты, когда ты встаешь, чтобы произнести речь.',
    'Они прочли лекцию насчет трезвости, но выручили такие гроши, что даже на выпивку не хватило.',
    'Никогда не спорьте с идиотами. Вы опуститесь до их уровня, где они вас задавят своим опытом.',
    'Единственный способ сохранить здоровье — это есть то, чего не хочешь, пить то, чего не любишь, и делать то, что не нравится.',
    'Работайте так, словно деньги не имеют для Вас никакого значения.',
    'Я когда-то работал на золотых приисках и знаю все о добыче золота, кроме лишь одного: как заработать там деньги.',
    'Лето — это время года, когда очень жарко, чтобы заниматься вещами, которыми заниматься зимой было очень холодно.',
    'Если вы не читаете газет — вы неинформированы. Если вы читаете газеты — вы дезинформированы.'
)

for i in text_all_time:
    @dp.message_handler(text_contains=i)
    async def text_contains_any_handler(message: types.Message):
        random_statments = random.randint(0, len(STATEMENTS)-1)
        await message.answer(STATEMENTS[random_statments])

list_data = ["game", "fox"]

def key_map():
    keyboard = types.InlineKeyboardMarkup()
    button = [
        types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
        types.InlineKeyboardButton(text="кнопка2", callback_data="value"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*button)
    return keyboard

for i in list_data:
    @dp.message_handler(regexp=f'({i}?)')
    async def cmd_random(message: types.Message):
        # keyboard = key_map()
        await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=key_map())
       

@dp.callback_query_handler(text="random_value")
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(random.randint(1, 10)))
    # with open('data/cats.jpg', 'rb') as photo:
    #     await call.message.reply_photo(photo, caption='Cats are here 😺')
    await call.answer()

@dp.callback_query_handler(text="value")
async def send_random_value(call: types.CallbackQuery):
    # await call.message.answer(str(random.randint(1, 10)))
    with open('data/cats.jpg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Cats are here 😺')
    await call.answer()

@dp.message_handler(regexp='(^cat[s]?)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')

if __name__ == '__main__':
    executor.start(dp, on_startup())
    executor.start_polling(dp, skip_updates=True)