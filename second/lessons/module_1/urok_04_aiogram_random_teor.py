# ============================================================
# ПРАКТИКУМ: РАНДОМ И ЛОГИКА В AIOGRAM
# Python AI-боты, урок 4 (М1У4)
# ============================================================

# ---------------------- 1 - активация модуля random

# random — встроенная библиотека Python (устанавливать не нужно).
# Она делает поведение бота живым и непредсказуемым.
import random


# ---------------------- 2 - генерация случайных чисел (random.randint)

# Возвращает случайное целое число в заданном диапазоне (включительно).
power = random.randint(1, 100)


# ---------------------- 3 - выбор из списка (random.choice)

# Возвращает случайный элемент из списка.
greetings = ["Здравствуй, Архитектор!", "Системы онлайн!", "Рад тебя видеть!"]
random_greeting = random.choice(greetings)


# ---------------------- 4 - валидация ввода (isdigit)

# Бот должен защитить себя от ошибок, если ждет число, а получает текст.
# isdigit() возвращает True, только если в строке ТОЛЬКО цифры.

# if message.text.isdigit():
#     # Если внутри строки только цифры — превращаем в число
#     user_num = int(message.text)
# else:
#     # Если там буквы или символы — выдаем предупреждение
#     await message.answer("Ошибка! Мои сенсоры распознают только числовые коды.")


# ---------------------- 5 - логические гейты (if/elif/else)

# message.text всегда строка (str).
# Чтобы сравнить с числом, приводим к int().
# Используем and и or для сложных условий.

# if power > 80:
#     status = "Критическое усиление! ⚡"
# elif power > 50:
#     status = "Системы в норме. 👍"
# else:
#     status = "Требуется подзарядка... 🪫"


# ---------------------- 6 - игра «Камень, ножницы, бумага»

# Фильтр F.text.lower().in_(["камень", "ножницы", "бумага"])
# ловит только эти слова в любом регистре.

# options = ["камень", "ножницы", "бумага"]
# bot_choice = random.choice(options)
# user_choice = message.text.lower()


# ---------------------- 7 - определение победителя

# Связки and и or позволяют описать сложные правила игры.

# if user_choice == bot_choice:
#     result = "Ничья! Системы уравновешены. 🤝"
# elif (user_choice == "камень" and bot_choice == "ножницы") or \
#      (user_choice == "ножницы" and bot_choice == "бумага") or \
#      (user_choice == "бумага" and bot_choice == "камень"):
#     result = f"Победа! Архитектор {message.from_user.first_name} взломал защиту! 🏆"
# else:
#     result = "Поражение... Дроид-Страж оказался сильнее. 🤖"


# ============================================================
# ТАБЛИЦА КЛАССОВ И МЕТОДОВ:
# ============================================================
# import random              | импорт модуля случайных чисел
# random.randint(a, b)       | случайное целое число от a до b
# random.choice(list)        | случайный элемент из списка
# message.text.isdigit()     | проверка, что строка состоит только из цифр
# int(message.text)          | преобразование строки в число
# F.text.lower().in_([...])  | фильтр на список слов в нижнем регистре
# ============================================================

# ============================================================
# КЛЮЧЕВЫЕ МОМЕНТЫ:
# ============================================================
# 1. random.randint(1, 100) — случайное число
# 2. random.choice() — случайный выбор из списка
# 3. isdigit() — защита от ошибок ввода (ожидаем число)
# 4. message.text — всегда строка, приводим к int()
# 5. F.text.lower().in_() — умный фильтр для текста
# 6. and / or — объединение условий для сложной логики


# ============================================================
# ФИНАЛЬНЫЙ КОД (собираем всё вместе):
# ============================================================

import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН")
dp = Dispatcher()


# --- Команда /roll (Система везения) ---
@dp.message(Command("roll"))
async def cmd_roll(message: types.Message):
    # Генерируем случайное число силы
    power = random.randint(1, 100)
    
    if power > 80:
        status = "Критическое усиление! ⚡"
    elif power > 50:
        status = "Системы в норме. 👍"
    else:
        status = "Требуется подзарядка... 🪫"
    
    await message.answer(f"Твой уровень мощности сегодня: {power}%\nСтатус: {status}")


# --- Валидатор «Числовой вход» ---
@dp.message(F.text)
async def check_number(message: types.Message):
    # Если пользователь написал команду, пропускаем (чтобы не мешать другим хэндлерам)
    if message.text.startswith("/"):
        return

    if message.text.isdigit():
        number = int(message.text)
        await message.answer(f"Принято число: {number}. Анализирую...")
    else:
        await message.answer("Ошибка! Мои сенсоры распознают только числовые коды.")


# --- Игра «Кибер-Дуэль» (Камень, ножницы, бумага) ---
@dp.message(F.text.lower().in_(["камень", "ножницы", "бумага"]))
async def cyber_duel(message: types.Message):
    # 1. Инвентарь дроида
    options = ["камень", "ножницы", "бумага"]
    
    # 2. Ход бота (Чип Хаоса)
    bot_choice = random.choice(options)
    user_choice = message.text.lower()
    
    # 3. Логические гейты (Определяем победителя)
    if user_choice == bot_choice:
        result = "Ничья! Системы уравновешены. 🤝"
    elif (user_choice == "камень" and bot_choice == "ножницы") or \
         (user_choice == "ножницы" and bot_choice == "бумага") or \
         (user_choice == "бумага" and bot_choice == "камень"):
        result = f"Победа! Архитектор {message.from_user.first_name} взломал защиту! 🏆"
    else:
        result = "Поражение... Дроид-Страж оказался сильнее. 🤖"
    
    # 4. Выдача результата
    await message.answer(f"Ты выбрал: {user_choice}\nМой выбор: {bot_choice}\n\n{result}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())