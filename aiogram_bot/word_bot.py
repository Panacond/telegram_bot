import logging, random, time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parse_site import weather_sinoptic, return_weather_data, weather_text
from token_pass import API_TOKEN
from work_data_base import read_data_weather, wrire_data_weather
import work_data_base
import aioschedule
import asyncio
from datetime import date

class TimerHelp():
    def __init__(self):
        self.start_time = 0
    
    def set_now_time(self):
        self.start_time = time.time()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
def down_keywords():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    buttons = ["погода Одесса", "Game", "dictionary", "добавить в словарь"]

    keyboard.add(*buttons)
    return keyboard

async def on_startup(_):
    asyncio.create_task(scheduler())
    user_should_be_notified = -702529372
    down_keyword = down_keywords()
    await bot.send_message(user_should_be_notified, "Бот перезапущен", reply_markup=down_keyword)

def get_keyboard():
    # Генерация клавиатуры.
    keyboard = types.InlineKeyboardMarkup()
    buttons = [
        types.InlineKeyboardButton(text="racoon", callback_data="racoon"),
        types.InlineKeyboardButton(text="dog", callback_data="dog"),
        types.InlineKeyboardButton(text="seagull", callback_data="seagull"),
        types.InlineKeyboardButton(text="squirrel", callback_data="squirrel"),
        types.InlineKeyboardButton(text="cat", callback_data="cat"),
        types.InlineKeyboardButton(text="fox", callback_data="fox")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    down_keyboard = down_keywords()
    await message.reply("""Hi!\nI'm Bot!\nI'm type some statements\nYou type words: мысль, идея, thought, idea, cat
идея и idea - отвечает срауз
мысль и thought - толькое если предыдущий запрос с этим словом был раньше получаса
En word - переводит слово на русский
Ру слово - переводит на английский""", reply_markup=down_keyboard)

@dp.message_handler(text="Game")
async def start_game(message: types.Message):
    await message.answer("Выберети животное", reply_markup=get_keyboard())

@dp.callback_query_handler(text='racoon')
async def start_game(call: types.CallbackQuery):
    with open('data/racoon.jpeg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Racoon is here', reply_markup=get_keyboard())
    await call.answer()

@dp.callback_query_handler(text='dog')
async def start_game(call: types.CallbackQuery):
    with open('data/dog.jpg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Dog is here', reply_markup=get_keyboard())
    await call.answer()

@dp.callback_query_handler(text='seagull')
async def start_game(call: types.CallbackQuery):
    with open('data/seagull.jpg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Seagull is here', reply_markup=get_keyboard())
    await call.answer()

@dp.callback_query_handler(text='squirrel')
async def start_game(call: types.CallbackQuery):
    with open('data/squirrel.jpeg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Sqaull is here', reply_markup=get_keyboard())
    await call.answer()

@dp.callback_query_handler(text='cat')
async def start_game(call: types.CallbackQuery):
    with open('data/mother_in_low_cat.jpg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Cats is here', reply_markup=get_keyboard())
    await call.answer()

@dp.callback_query_handler(text="fox")
async def start_game(call: types.CallbackQuery):
    with open('data/fox.jpg', 'rb') as photo:
        await call.message.reply_photo(photo, caption='Fox is here', reply_markup=get_keyboard())
    await call.answer()

text_all_time=('мысль', 'thought')
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

text_in_period=('идея', 'idea')
data_time = TimerHelp()

for i in text_in_period:
    @dp.message_handler(text_contains=i)
    async def text_contains_any_handler(message: types.Message):
        difference = time.time() - data_time.start_time
        if difference > 10:
            data_time.set_now_time()
            random_statment = random.randint(0, len(STATEMENTS)-1)
            await message.answer(STATEMENTS[random_statment])

@dp.message_handler(Text(equals="погода Одесса"))
async def with_puree(message: types.Message):
    today = date.today()
    data_now = today.strftime("%Y-%m-%d")
    text =  weather_text(read_data_weather(data_now))
    weather_sinoptic()
    await message.answer(weather_sinoptic())

async def get_weather():
    list_weather = return_weather_data("https://sinoptik.ua/погода-одесса")
    today = date.today()
    data_now = today.strftime("%Y-%m-%d")
    wrire_data_weather(data_weather=data_now, list_temp=list_weather)
    user_id = -702529372
    text =  weather_text(read_data_weather(data_now))
    await bot.send_message(user_id, text)
    print(data_now)

async def scheduler():
    aioschedule.every().day.at("0:00").do(get_weather)
    # aioschedule.every(1).minutes.do(get_weather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

@dp.message_handler(regexp='(^cat[s]?)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')

@dp.message_handler(regexp='(^en ?)')
@dp.message_handler(regexp='(^En ?)')
@dp.message_handler(regexp='(^ру ?)')
@dp.message_handler(regexp='(^Ру ?)')
async def cats(message: types.Message):
    text = message.text
    text = text.rstrip()
    text = work_data_base.search_word(text)
    await message.answer(text)

@dp.message_handler(Text(equals="dictionary"))
async def with_puree(message: types.Message):
    await message.answer(work_data_base.dictionary_list())

@dp.message_handler(text="добавить в словарь")
async def start_game(message: types.Message):
    await message.answer("Введите словов в формате:\n word - слово",)

@dp.message_handler(regexp='(.* - .*)')
async def add_dictionary(message: types.Message):
    text_message = work_data_base.add_to_dictionary(message.text)
    await message.answer(text_message)

if __name__ == '__main__':
    # executor.start(dp, on_startup())
    # executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


    