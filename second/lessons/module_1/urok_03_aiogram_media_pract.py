# ============================================================
# РАБОТА С МЕДИА - ПРАКТИЧЕСКАЯ РАБОТА
# Python AI-боты, урок 3 (М1У3)
# ============================================================

# ============================================================
# ЗАДАЧА №1 (Уровень junior — «Механик»):
# 1. Подготовь картинку meme.jpg в папке с проектом.
# 2. Добавь import FSInputFile.
# 3. Напиши хэндлер для команды /photo.
# ============================================================

# Решение:
#
# from aiogram.types import FSInputFile
#
# @dp.message(Command("photo"))
# async def send_meme(message: types.Message):
#     photo_file = FSInputFile("meme.jpg")
#     await message.answer_photo(photo=photo_file, caption="Мой мем!")


# ============================================================
# ЗАДАЧА №2 (Уровень middle — «Инженер»):
# Персонализировать систему: изменить подпись к фото,
# используя f-строку и имя пользователя.
# ============================================================

# Решение:
#
# @dp.message(Command("photo"))
# async def send_meme(message: types.Message):
#     photo_file = FSInputFile("meme.jpg")
#     user_name = message.from_user.first_name
#     await message.answer_photo(
#         photo=photo_file,
#         caption=f"Архитектор {user_name}, ваш секретный чертеж загружен!"
#     )


# ============================================================
# ЗАДАЧА №3 (Уровень senior — «Изобретатель»):
# Создать модуль «Случайная схема».
# По команде /random_photo бот отправляет случайную картинку
# из списка (1.jpg, 2.jpg, 3.jpg).
# ============================================================

# Решение:
#
# import random
#
# images = ["1.jpg", "2.jpg", "3.jpg"]
#
# @dp.message(Command("random_photo"))
# async def send_random_meme(message: types.Message):
#     random_image = random.choice(images)
#     photo_file = FSInputFile(random_image)
#     await message.answer_photo(
#         photo=photo_file,
#         caption=f"Случайная схема: {random_image}"
#     )


# ============================================================
# ЗАДАЧА №1 (Уровень junior — «Механик» - File ID):
# 1. Отправить боту любую картинку, чтобы узнать ID.
# 2. Создать команду /show_id для отправки фото по ID.
# ============================================================

# Решение:
#
# @dp.message(Command("show_id"))
# async def show_id(message: types.Message):
#     saved_file_id = "AgACAgIAAxkBAAI..."  # Вставь свой ID
#     await message.answer_photo(
#         photo=saved_file_id,
#         caption="Это фото отправлено по ID!"
#     )


# ============================================================
# ЗАДАЧА №2 (Уровень middle — «Визуальное приветствие»):
# По команде /start бот отправляет картинку по File ID
# и приветствует пользователя по имени.
# ============================================================

# Решение:
#
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     welcome_id = "AgACAgIAAxkBAAI..."  # ID приветственной картинки
#     user_name = message.from_user.first_name
#     await message.answer_photo(
#         photo=welcome_id,
#         caption=f"Добро пожаловать в систему, Архитектор {user_name}! Твой пропуск активен."
#     )


# ============================================================
# ЗАДАЧА №3 (Уровень senior — «Мгновенный обмен»):
# Создать gallery = [].
# При получении фото добавлять ID в gallery.
# По команде /send_all отправлять все фото из списка.
# ============================================================

# Решение:
#
# gallery = []
#
# @dp.message(F.photo)
# async def get_file_id(message: types.Message):
#     file_id = message.photo[-1].file_id
#     gallery.append(file_id)
#     await message.answer(f"Код добавлен в галерею! Всего фото: {len(gallery)}")
#
# @dp.message(Command("send_all"))
# async def send_all_photos(message: types.Message):
#     if not gallery:
#         await message.answer("Галерея пуста!")
#         return
#     for file_id in gallery:
#         await message.answer_photo(photo=file_id)


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень junior):
# Команда /help_media. Бот присылает видео-инструкцию
# (используй answer_video и file_id).
# ============================================================

# Решение:
#
# @dp.message(Command("help_media"))
# async def send_video(message: types.Message):
#     video_id = "ВАШ_FILE_ID_ВИДЕО"
#     await message.answer_video(
#         video=video_id,
#         caption="Смотри видео-инструкцию, Архитектор!"
#     )


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень middle):
# Команда /my_card. Бот присылает фото (по file_id)
# и пишет в подписи имя и ID пользователя из message.from_user.
# ============================================================

# Решение:
#
# @dp.message(Command("my_card"))
# async def my_card(message: types.Message):
#     card_id = "ВАШ_FILE_ID_ФОТО"
#     name = message.from_user.first_name
#     user_id = message.from_user.id
#     await message.answer_photo(
#         photo=card_id,
#         caption=f"Имя: {name}\nID: {user_id}\nСтатус: Архитектор"
#     )


# ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ (Уровень senior):
# Команда /album. Бот отправляет 3 разных фото из списка file_id
# одно за другим (через цикл for).
# ============================================================

# Решение:
#
# @dp.message(Command("album"))
# async def send_album(message: types.Message):
#     album = [
#         "FILE_ID_КАРТИНКИ_1",
#         "FILE_ID_КАРТИНКИ_2",
#         "FILE_ID_КАРТИНКИ_3"
#     ]
#     await message.answer("Загружаю секретный альбом... 📂")
#     for photo_id in album:
#         await message.answer_photo(photo=photo_id)


# ============================================================
# ФИНАЛЬНЫЙ КОД ДЛЯ ПРОВЕРКИ (все задания + ДЗ в одном файле):
# ============================================================

import asyncio
import logging
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)
bot = Bot(token="ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН")
dp = Dispatcher()

# Глобальное хранилище для галереи
gallery = []


# --- /start с картинкой и приветствием (Middle) ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_id = "AgACAgIAAxkBAAI..."  # Замени на свой ID
    name = message.from_user.first_name
    await message.answer_photo(
        photo=welcome_id,
        caption=f"Добро пожаловать, {name}! Твой пропуск активен."
    )


# --- Отправка мема с компьютера (Junior + Middle) ---
@dp.message(Command("photo"))
async def send_meme(message: types.Message):
    try:
        photo_file = FSInputFile("meme.jpg")
        name = message.from_user.first_name
        await message.answer_photo(
            photo=photo_file,
            caption=f"Архитектор {name}, лови мой любимый мем! 🐱"
        )
    except FileNotFoundError:
        await message.answer("Файл meme.jpg не найден!")


# --- Случайная картинка (Senior) ---
@dp.message(Command("random_photo"))
async def send_random(message: types.Message):
    images = ["1.jpg", "2.jpg", "3.jpg"]
    random_image = random.choice(images)
    await message.answer_photo(
        photo=FSInputFile(random_image),
        caption=f"Случайная схема: {random_image}"
    )


# --- Ловушка для фото: получаем ID и добавляем в галерею (Senior) ---
@dp.message(F.photo)
async def get_file_id(message: types.Message):
    file_id = message.photo[-1].file_id
    gallery.append(file_id)
    await message.answer(f"Код добавлен в галерею! Всего фото: {len(gallery)}")


# --- Отправка всех фото из галереи (Senior) ---
@dp.message(Command("send_all"))
async def send_all_photos(message: types.Message):
    if not gallery:
        await message.answer("Галерея пуста!")
        return
    for file_id in gallery:
        await message.answer_photo(photo=file_id)


# --- ДЗ Junior: Видео-инструкция ---
@dp.message(Command("help_media"))
async def send_video(message: types.Message):
    video_id = "ВАШ_FILE_ID_ВИДЕО"
    await message.answer_video(
        video=video_id,
        caption="Смотри видео-инструкцию, Архитектор!"
    )


# --- ДЗ Middle: Визитная карточка ---
@dp.message(Command("my_card"))
async def my_card(message: types.Message):
    card_id = "ВАШ_FILE_ID_ФОТО"
    name = message.from_user.first_name
    user_id = message.from_user.id
    await message.answer_photo(
        photo=card_id,
        caption=f"Имя: {name}\nID: {user_id}\nСтатус: Архитектор"
    )


# --- ДЗ Senior: Секретный альбом из 3 фото ---
@dp.message(Command("album"))
async def send_album(message: types.Message):
    album = [
        "FILE_ID_КАРТИНКИ_1",
        "FILE_ID_КАРТИНКИ_2",
        "FILE_ID_КАРТИНКИ_3"
    ]
    await message.answer("Загружаю секретный альбом... 📂")
    for photo_id in album:
        await message.answer_photo(photo=photo_id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())