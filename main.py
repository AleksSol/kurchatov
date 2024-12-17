import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio

import random


def generate():
    names = ['Крош', 'Халк', 'Человек Паук', 'КарКарыч', 'Лосяш', 'Железный Человек']
    return names[random.randint(0, 5)]


translit_dict = {
    # Русская -> Английская
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[',
    'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';',
    'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.',

    # Заглавные буквы
    'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{',
    'Ъ': '}', 'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':',
    'Э': '"', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N', 'Ь': 'M', 'Б': '<', 'Ю': '>',

    # Английская -> Русская
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': '[',
    ']': ']', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': ';',
    "'": "'", 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': ',', '.': '.',

    # Заглавные английские -> Русские
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': '{',
    '}': '}', 'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', ':': ':',
    '"': '"', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', '<': '<', '>': '>',
}

def transliterate(text):
    return ''.join(translit_dict.get(char, char) for char in text)

API_TOKEN = ''

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("check"))
async def command_check(message: types.Message):
    await message.answer("Привет! Я простейший бот на aiogram. Используй /help для получения информации.")


@dp.message(Command("generate"))
async def commang_generate(message: types.Message):
    val = generate()
    await message.answer(val)


# обработка текста
@dp.message(F.text)
async def echo(message: types.Message):
    msg_text = message.text
    if msg_text[-1] != '?':
        ans_text = transliterate(msg_text)
        await message.answer(ans_text)
    else:
        pass


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
