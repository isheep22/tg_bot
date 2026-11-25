# ============================================================
# ЭХО-БОТ И АСИНХРОННОСТЬ - ПРАКТИЧЕСКАЯ РАБОТА
# Python AI-боты, урок 2 (М1У2)
# ============================================================

# ============================================================
# ЗАДАЧА №1 (Уровень junior — «Вежливый сканер»):
# Научить бота обращаться по имени.
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def echo_mirror(message: types.Message):
#     await message.answer(
#         f"{message.from_user.first_name}, ты написал: {message.text}"
#     )


# ============================================================
# ЗАДАЧА №2 (Уровень middle — «Бот-аналитик»):
# Бот должен посчитать количество символов в тексте.
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def echo_mirror(message: types.Message):
#     length = len(message.text)
#     await message.answer(
#         f"{message.from_user.first_name}, в твоем сообщении {length} символов!"
#     )


# ============================================================
# ЗАДАЧА №3 (Уровень senior — «Ловушка для стикеров»):
# Если прислать наклейку — узнать ID и отправить её же обратно.
# ============================================================

# Решение:
#
# @dp.message(F.sticker)
# async def sticker_handler(message: types.Message):
#     await message.answer_sticker(message.sticker.file_id)
#     await message.answer(
#         f"Я сохранил паспортный номер этого стикера: {message.sticker.file_id}"
#     )


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень junior):
# «Крик в космосе»
# Бот работает как эхо, но возвращает текст в ВЕРХНЕМ РЕГИСТРЕ.
# Пример: «привет» -> «ПРИВЕТ!»
# Подсказка: метод строки .upper()
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def scream_bot(message: types.Message):
#     await message.answer(message.text.upper())


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень middle):
# «Зеркальный код»
# Бот отвечает по имени, переворачивает текст и приписывает длину.
# Пример: «Python» -> «Иван, твой перевернутый текст: nohtyP. Длина: 6»
# Подсказка: срез [::-1] и функция len()
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def mirror_bot(message: types.Message):
#     reversed_text = message.text[::-1]
#     length = len(message.text)
#     await message.answer(
#         f"{message.from_user.first_name}, твой перевернутый текст: {reversed_text}. Длина: {length}"
#     )


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень senior):
# «Детектив контента»
# Бот распознает типы данных и ведет статистику:
# 1. Текст: «Вижу текст! В нем [число] слов». (Подсказка: .split())
# 2. Стикер: «Вижу стикер! Его ID: [file_id]».
# 3. Фото/Видео: «Я пока не умею это обрабатывать, но скоро научусь!».
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def text_detective(message: types.Message):
#     words = len(message.text.split())
#     await message.answer(f"Вижу текст! В нем {words} слов.")
#
#
# @dp.message(F.sticker)
# async def sticker_detective(message: types.Message):
#     await message.answer(f"Вижу стикер! Его паспортный ID: {message.sticker.file_id}")
#
#
# # ВАЖНО: Общий хэндлер должен быть САМЫМ ПОСЛЕДНИМ, чтобы не перехватывать
# # текстовые сообщения и стикеры, которые мы уже обработали выше.
# @dp.message()
# async def other_detective(message: types.Message):
#     await message.answer("Я пока не умею это обрабатывать, но скоро научусь!")


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
    await message.answer(f"Привет, {message.from_user.first_name}! Я готов к работе!")


# --- Junior: Крик в космосе ---
@dp.message(F.text)
async def scream_bot(message: types.Message):
    await message.answer(message.text.upper())


# --- Middle: Зеркальный код ---
@dp.message(F.text)
async def mirror_bot(message: types.Message):
    reversed_text = message.text[::-1]
    length = len(message.text)
    await message.answer(
        f"{message.from_user.first_name}, твой перевернутый текст: {reversed_text}. Длина: {length}"
    )


# --- Senior: Детектив контента ---
@dp.message(F.text)
async def text_detective(message: types.Message):
    words = len(message.text.split())
    await message.answer(f"Вижу текст! В нем {words} слов.")


@dp.message(F.sticker)
async def sticker_detective(message: types.Message):
    await message.answer(f"Вижу стикер! Его паспортный ID: {message.sticker.file_id}")


@dp.message()
async def other_detective(message: types.Message):
    await message.answer("Я пока не умею это обрабатывать, но скоро научусь!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())