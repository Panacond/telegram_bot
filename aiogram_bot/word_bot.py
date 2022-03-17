import logging, random, time
from threading import Timer
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parse_site import weather_sinoptic

class TimerHelp():
    def __init__(self):
        self.start_time = 0
    
    def set_now_time(self):
        self.start_time = time.time()

API_TOKEN = '1426091599:AAH0FiP0WvsVXCJ74FKpQTUMrp87bzuZcck'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["погода Одесса"]
    keyboard.add(*buttons)
    await message.reply("Hi!\nI'm Bot!\nI'm type some statements\nYou type words: мысль, идея, thought, idea, cat", reply_markup=keyboard)

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
    await message.answer(weather_sinoptic())


@dp.message_handler(regexp='(^cat[s]?)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await message.reply_photo(photo, caption='Cats are here 😺')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    