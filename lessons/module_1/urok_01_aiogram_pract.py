# ============================================================
# ЗНАКОМСТВО С AIOGRAM - ПРАКТИЧЕСКАЯ РАБОТА
# Python AI-боты, урок 1 (М1У1)
# ============================================================

# ============================================================
# ЗАДАЧА №1 (Уровень junior — "Механик"):
# Заставить код работать.
# 1. Скопируйте код из теории.
# 2. Вставьте СВОЙ токен от BotFather.
# 3. Запустите программу.
# 4. Напишите боту /start в Telegram.
# ============================================================

# Решение:
# (Скопировать финальный код из теории,
#  заменить "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН" на свой токен)


# ============================================================
# ЗАДАЧА №2 (Уровень middle — "Инженер"):
# Научить бота вежливости: называть пользователя по имени.
# Подсказка: message.from_user.first_name
# ============================================================

# Решение:
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer(
#         f"Привет, {message.from_user.first_name}! Я проснулся!"
#     )


# ============================================================
# ЗАДАЧА №3 (Уровень senior — "Изобретатель"):
# Научить бота реагировать на любой текст (эхо-бот).
# 1. Добавить from aiogram import F
# 2. Создать новый хэндлер с фильтром F.text
# 3. Челлендж: бот повторяет текст + смайлик
# ============================================================

# Решение:
#
# from aiogram import F
#
# @dp.message(F.text)
# async def echo_handler(message: types.Message):
#     await message.answer(f"{message.text} 🐱")


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень junior):
# «Расширение протоколов»
# Добавить второй хэндлер на команду /help.
# Ответ: "Это бот-помощник. Я пока ничего не умею, но скоро научусь!"
# ============================================================

# Решение:
#
# @dp.message(Command("help"))
# async def cmd_help(message: types.Message):
#     await message.answer(
#         "Это бот-помощник. Я пока ничего не умею, но скоро научусь!"
#     )


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень middle):
# «Двойной залп»
# На команду /start отправлять ДВА сообщения подряд:
# 1. "Запуск систем..."
# 2. "Бот готов к работе!"
# ============================================================

# Решение:
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Запуск систем...")
#     await message.answer("Бот готов к работе!")


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень senior):
# «Ремонт Дроида» (Debug)
# В коде 3 критические ошибки. Найти, исправить, запустить.
#
# Сломанный код:
# dp.message(Command("start"))
# async def cmd_start(message: Message):
#     message.answer("Привет!")
#
# async def main():
#     await dp.start_polling(bot)
# ============================================================

# Решение:
#
# Ошибка 1: пропущен декоратор @ перед dp.message
# Ошибка 2: пропущен await перед message.answer
# Ошибка 3: не создан объект bot (bot = Bot(token="..."))
#
# Исправленный код:
#
# bot = Bot(token="ТВОЙ_ТОКЕН")
# dp = Dispatcher()
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет!")
#
# async def main():
#     await dp.start_polling(bot)
#
# if __name__ == "__main__":
#     asyncio.run(main())


# ============================================================
# ФИНАЛЬНЫЙ КОД ДЛЯ ПРОВЕРКИ (все задания + ДЗ):
# ============================================================

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Запуск систем...")
    await message.answer(
        f"Привет, {message.from_user.first_name}! Бот готов к работе!"
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Это бот-помощник. Я пока ничего не умею, но скоро научусь!"
    )


@dp.message(F.text)
async def echo_handler(message: types.Message):
    await message.answer(f"{message.text} 🐱")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())