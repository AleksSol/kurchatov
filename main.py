
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio

import random

def generate():
    names = ['Крош', 'Халк', 'Человек Паук', 'КарКарыч', 'Лосяш', 'Железный Человек']
    return names[random.randint(0, 5)]

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("check"))
async def command_check(message: types.Message):
    await message.answer("Привет! Я простейший бот на aiogram. Используй /help для получения информации.")

@dp.message(Command("generate"))
async def commang_generate(message: types.Message):
    val=generate()
    await message.answer(val)

#обработка текста
@dp.message(F.text)
async def echo(message: types.Message):
    msg_text=message.text


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

