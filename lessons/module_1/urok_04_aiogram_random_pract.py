# ============================================================
# ПРАКТИКУМ: РАНДОМ И ЛОГИКА - ПРАКТИЧЕСКАЯ РАБОТА
# Python AI-боты, урок 4 (М1У4)
# ============================================================

# ============================================================
# ЗАДАНИЕ №1 (Уровень junior):
# Создать команду /roll.
# Бот генерирует число от 1 до 100 и выдает статус в зависимости от него.
# ============================================================

# Решение:
#
# @dp.message(Command("roll"))
# async def cmd_roll(message: types.Message):
#     power = random.randint(1, 100)
#     if power > 80:
#         status = "Критическое усиление! ⚡"
#     elif power > 50:
#         status = "Системы в норме. 👍"
#     else:
#         status = "Требуется подзарядка... 🪫"
#     await message.answer(f"Твой уровень мощности сегодня: {power}%\nСтатус: {status}")


# ============================================================
# ЗАДАНИЕ №2 (Уровень middle):
# Создать «умный гейт» — валидатор числового ввода.
# Если пользователь присылает число — бот его принимает.
# Если текст — выдает ошибку через isdigit().
# ============================================================

# Решение:
#
# @dp.message(F.text)
# async def check_number(message: types.Message):
#     if message.text.isdigit():
#         number = int(message.text)
#         await message.answer(f"Принято число: {number}. Анализирую...")
#     else:
#         await message.answer("Ошибка! Мои сенсоры распознают только числовые коды.")


# ============================================================
# ЗАДАНИЕ №3 (Уровень senior):
# Собрать игру «Кибер-Дуэль» (Камень, ножницы, бумага).
# Бот отвечает на эти слова в любом регистре и определяет победителя.
# ============================================================

# Решение:
#
# @dp.message(F.text.lower().in_(["камень", "ножницы", "бумага"]))
# async def cyber_duel(message: types.Message):
#     options = ["камень", "ножницы", "бумага"]
#     bot_choice = random.choice(options)
#     user_choice = message.text.lower()
#     
#     if user_choice == bot_choice:
#         result = "Ничья! Системы уравновешены. 🤝"
#     elif (user_choice == "камень" and bot_choice == "ножницы") or \
#          (user_choice == "ножницы" and bot_choice == "бумага") or \
#          (user_choice == "бумага" and bot_choice == "камень"):
#         result = f"Победа! Архитектор {message.from_user.first_name} взломал защиту! 🏆"
#     else:
#         result = "Поражение... Дроид-Страж оказался сильнее. 🤖"
#     
#     await message.answer(f"Ты выбрал: {user_choice}\nМой выбор: {bot_choice}\n\n{result}")


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень junior):
# «Кости»: Создать команду /dice.
# Бот генерирует два случайных числа от 1 до 6 и пишет их сумму.
# ============================================================

# Решение:
#
# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     await message.answer(f"🎲 Кубик 1: {dice1}\n🎲 Кубик 2: {dice2}\nСумма: {dice1 + dice2}")


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень middle):
# «Охота на стикеры»: Используй фильтр F.sticker.
# Если прислали стикер, бот бросает монетку (randint(1, 2)).
# 1 — хвалит, 2 — ругает.
# ============================================================

# Решение:
#
# @dp.message(F.sticker)
# async def sticker_hunt(message: types.Message):
#     coin = random.randint(1, 2)
#     if coin == 1:
#         await message.answer("Отличный стикер! 🏆")
#     else:
#         await message.answer("Фу, какой скучный стикер! 🥱")


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень senior):
# «Секретный фотоальбом»: Список из 5 file_id.
# По команде /surprise отправляет случайную.
# Если выпала 1-я или 5-я — добавляет подпись «Легендарная карта!».
# ============================================================

# Решение:
#
# @dp.message(Command("surprise"))
# async def cmd_surprise(message: types.Message):
#     album = ["ID1", "ID2", "ID3", "ID4", "ID5"] # Заменить на реальные ID
#     chosen_index = random.randint(0, 4)
#     chosen_photo = album[chosen_index]
#     
#     caption = "Обычная карта."
#     if chosen_index == 0 or chosen_index == 4:
#         caption = "Тебе выпала легендарная карта! 🌟"
#         
#     await message.answer_photo(photo=chosen_photo, caption=caption)


# ============================================================
# ФИНАЛЬНЫЙ КОД ДЛЯ ПРОВЕРКИ (все задания + ДЗ в одном файле):
# ============================================================

import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН")
dp = Dispatcher()


# --- /roll ---
@dp.message(Command("roll"))
async def cmd_roll(message: types.Message):
    power = random.randint(1, 100)
    if power > 80:
        status = "Критическое усиление! ⚡"
    elif power > 50:
        status = "Системы в норме. 👍"
    else:
        status = "Требуется подзарядка... 🪫"
    await message.answer(f"Твой уровень мощности сегодня: {power}%\nСтатус: {status}")


# --- /dice (ДЗ Junior) ---
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    await message.answer(f"🎲 Кубик 1: {dice1}\n🎲 Кубик 2: {dice2}\nСумма: {dice1 + dice2}")


# --- /surprise (ДЗ Senior) ---
@dp.message(Command("surprise"))
async def cmd_surprise(message: types.Message):
    album = [
        "AgACAgIAAxkBAAI...", # Замени на реальные file_id
        "AgACAgIAAxkBAAI...",
        "AgACAgIAAxkBAAI...",
        "AgACAgIAAxkBAAI...",
        "AgACAgIAAxkBAAI..."
    ]
    chosen_index = random.randint(0, 4)
    chosen_photo = album[chosen_index]
    
    caption = "Обычная карта."
    if chosen_index == 0 or chosen_index == 4:
        caption = "Тебе выпала легендарная карта! 🌟"
        
    await message.answer_photo(photo=chosen_photo, caption=caption)


# --- Валидатор текста ---
@dp.message(F.text)
async def check_number(message: types.Message):
    if message.text.startswith("/"):
        return
    if message.text.isdigit():
        number = int(message.text)
        await message.answer(f"Принято число: {number}. Анализирую...")
    else:
        await message.answer("Ошибка! Мои сенсоры распознают только числовые коды.")


# --- Кибер-Дуэль ---
@dp.message(F.text.lower().in_(["камень", "ножницы", "бумага"]))
async def cyber_duel(message: types.Message):
    options = ["камень", "ножницы", "бумага"]
    bot_choice = random.choice(options)
    user_choice = message.text.lower()
    
    if user_choice == bot_choice:
        result = "Ничья! Системы уравновешены. 🤝"
    elif (user_choice == "камень" and bot_choice == "ножницы") or \
         (user_choice == "ножницы" and bot_choice == "бумага") or \
         (user_choice == "бумага" and bot_choice == "камень"):
        result = f"Победа! Архитектор {message.from_user.first_name} взломал защиту! 🏆"
    else:
        result = "Поражение... Дроид-Страж оказался сильнее. 🤖"
    
    await message.answer(f"Ты выбрал: {user_choice}\nМой выбор: {bot_choice}\n\n{result}")


# --- Стикер-Хант (ДЗ Middle) ---
@dp.message(F.sticker)
async def sticker_hunt(message: types.Message):
    coin = random.randint(1, 2)
    if coin == 1:
        await message.answer("Отличный стикер! 🏆")
    else:
        await message.answer("Фу, какой скучный стикер! 🥱")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())