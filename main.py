import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import keybords as kb
TOKEN = '5211324790:AAEWzTG-idWayLcVaIE3N5tfhIfS2HveP6M'

bot = Bot(token=TOKEN)  # Инициализация бота
dp = Dispatcher(bot, storage=MemoryStorage())
NOTIFICATION = 0
owner_id = 422948650


data = kb.DataClass()


@dp.message_handler(commands=['start'])  # Обработка команды
async def process_start_command(message: types.Message):
    await message.answer("Привет! Это бот про аналоги компаний.", reply_markup=data.categories_kb())
    if NOTIFICATION:
        await bot.send_message(owner_id, str(message.from_user.username) + ' что-то пишет боту')


@dp.message_handler(commands=['add'])  # Обработка команды
async def process_start_command(message: types.Message):
    if message.from_user.id == owner_id:
        cat = message.text.split()[1]
        company = message.text.split()[2]
        addition = message.text.split()[3] + ' - ' + message.text.split()[4]
        if company in data.companies.keys():
            data.companies[company] += '\n' + addition
        else:
            data.companies[company] = addition
    await message.answer('Отлично, обновили!')


@dp.message_handler(text=['Меню'])  # Обработка команды
async def process_start_command(message: types.Message):
    if NOTIFICATION:
        await bot.send_message(owner_id, str(message.from_user.username) + ' что-то пишет боту')
    await message.answer('Вы в главном меню', reply_markup=data.categories_kb())


@dp.message_handler()  # Обработка команды
async def process_start_command(message: types.Message):
    if message.text in data.categories:
        await message.answer('Вот список компаний', reply_markup=data.companies_kb(message.text))
    if message.text in data.companies.keys():
        await message.answer(data.compaines_text(message.text), reply_markup=data.back_to_menu())

if __name__ == '__main__':
    print("MAIN STARTED")
    executor.start_polling(dp, skip_updates=True)  # Запуск executor

