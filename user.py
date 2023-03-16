from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from src.services.sql import DataBase
from src.bot import bot, dp

from aiogram.dispatcher import FSMContext
from src.states.user import Machine
from src.keyboards.menu import starti
from aiogram import types
from datetime import datetime, timedelta

import random
usersers: dict = {}

dict = {
    'key' : {
        "key1":'1',
        "key2":"2"
    }
}
db = DataBase('vosk_database.db')

@dp.message_handler(Command('start'))
async def start(message: Message):
    power = random.randint(1, 100)
    height = random.randint(1, 100)
    await db.add_users(message.chat.id)
    await db.add_set(power, height, message.chat.id)
    await bot.send_message(message.chat.id, f'Привет, тебе выдано {power} силы, {height} здоровья, сейчас они записаны в базу данных, так же как и твой юзер айди', reply_markup=starti)

@dp.message_handler(text = ('Добавить значения в словарь'))
async def start(message: Message):
    user_id = message.chat.id
    power = await db.view_power(user_id)
    height = await db.view_height(user_id)
    usersers[f"{user_id}"] = {'power': f'{power[0][0]}', 'height': f'{height[0][0]}'}
    await bot.send_message(message.chat.id, "Данные успешно занесены в словарь")
    print(usersers)

@dp.message_handler(text = ('Вывести значения со словаря'))
async def start(message: Message):
    user_id = message.chat.id
    await bot.send_message(message.chat.id, f"{usersers}")
    await bot.send_message(message.chat.id, f"Вывод из словаря:\nВаша сила: {usersers[f'{user_id}']['power']}\nВаше здоровье: {usersers[f'{user_id}']['height']}")
