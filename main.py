import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio

import random

def generate():
    names = ['Крош', 'Халк', 'Человек Паук', 'КарКарыч', 'Лосяш', 'Железный Человек']
    return names[random.randint(0, 5)]

def check_eq(a,b):
    cnt=0
    na=len(a)
    nb=len(b)
    if na!=nb:
        return False
    for i in range(na):
        if a[i]!=b[i]:
            cnt+=1
    if cnt<=1:
        return True
    return False

API_TOKEN = '7854770916:AAGH4911WbTRujq3F7DYHWpJRV_PmjyeyYg'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("check"))
async def command_check(message: types.Message):
    s=message.text
    val=s.split(" ")

    if len(val)!=3:
        await message.answer("Введены не два слова")
    else:
        ans=check_eq(val[1],val[2])

        if ans:
            await message.answer("да")
        else:
            await message.answer("нет")


@dp.message(Command("generate"))
async def commang_generate(message: types.Message):
    val = generate()
    await message.answer(val)

# обработка текста
@dp.message(F.text)
async def echo(message: types.Message):
    if message.text[len(message.text) - 1] == '?':
        await message.answer('Не знаю')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
