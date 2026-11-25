# ============================================================
# РАБОТА С МЕДИА (ФОТО/ВИДЕО) В AIOGRAM
# Python AI-боты, урок 3 (М1У3)
# ============================================================

# ---------------------- 1 - локальный файл против File ID

# У бота есть два способа отправить картинку:
#
# 1. Локальный файл (FSInputFile):
#    Бот берет файл с вашего компьютера и каждый раз загружает его на сервера Telegram.
#    Это тратит время и интернет-трафик (как нести тяжелый ящик на почту).
#
# 2. File ID:
#    Файл уже один раз загружен на сервера Telegram.
#    Бот просто отправляет короткий код (ID), и Telegram мгновенно показывает файл.
#    Это быстро и экономит трафик.


# ---------------------- 2 - отправка файла с компьютера (FSInputFile)

# Чтобы бот мог "увидеть" файл на вашем диске, используем инструмент FSInputFile.
# Добавляем импорт в начало кода:
from aiogram.types import FSInputFile


# Создаем ловушку на команду /photo
@dp.message(Command("photo"))
async def send_meme(message: types.Message):
    # 1. Указываем путь к файлу (он должен лежать в папке с проектом)
    photo_file = FSInputFile("meme.jpg")
    
    # 2. Отправляем фото
    # answer_photo имеет два отсека: photo (файл или ID) и caption (подпись)
    await message.answer_photo(
        photo=photo_file,
        caption="Лови мой любимый мем! 🐱"
    )


# ---------------------- 3 - получение File ID из сообщения

# Чтобы узнать ID картинки, нужно ее перехватить.
# Фильтр F.photo ловит сообщения с картинками.
# message.photo — это список картинок в разных размерах.
# Индекс [-1] берет самую большую и качественную.

@dp.message(F.photo)
async def get_file_id(message: types.Message):
    # Получаем ID картинки
    file_id = message.photo[-1].file_id
    
    # Отправляем ID пользователю
    await message.answer(f"Секретный код этого файла получен:\n{file_id}")


# ---------------------- 4 - отправка медиа по File ID

# Если у вас уже есть ID картинки (скопировали ранее),
# можно отправить ее без FSInputFile, просто передав строку с ID.

@dp.message(Command("show_id"))
async def show_by_id(message: types.Message):
    # Вставляем ранее полученный ID (строка)
    saved_file_id = "AgACAgIAAxkBAAI..."
    
    await message.answer_photo(
        photo=saved_file_id,
        caption="Это фото отправлено по ID!"
    )


# ---------------------- 5 - отправка видео

# Для видео используется метод answer_video.
# Логика точно такая же: либо FSInputFile, либо File ID.

# await message.answer_video(
#     video=video_file_id,
#     caption="Смотри видео-инструкцию!"
# )


# ============================================================
# ТАБЛИЦА КЛАССОВ И МЕТОДОВ:
# ============================================================
# FSInputFile("path")        | загрузка файла с компьютера
# message.answer_photo()     | отправка фото
# message.answer_video()     | отправка видео
# photo=...                  | параметр для файла или ID
# caption=...                | текстовая подпись под медиа
# F.photo                    | фильтр сообщений с фото
# message.photo[-1].file_id  | получение ID самого качественного фото
# ============================================================

# ============================================================
# КЛЮЧЕВЫЕ МОМЕНТЫ:
# ============================================================
# 1. FSInputFile — берет файл с компьютера (каждый раз грузит заново)
# 2. File ID — мгновенная отправка файла, который уже есть в Telegram
# 3. answer_photo(photo=..., caption=...) — для фото
# 4. answer_video(video=..., caption=...) — для видео
# 5. F.photo — фильтр для картинок
# 6. message.photo[-1] — самый большой размер фото
# 7. file_id — уникальный код файла в Telegram


# ============================================================
# ФИНАЛЬНЫЙ КОД (собираем всё вместе):
# ============================================================

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(token="ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН")
dp = Dispatcher()


# --- Отправка файла с компьютера ---
@dp.message(Command("photo"))
async def send_meme(message: types.Message):
    try:
        photo_file = FSInputFile("meme.jpg")
        await message.answer_photo(
            photo=photo_file,
            caption="Лови мой любимый мем! 🐱"
        )
    except FileNotFoundError:
        await message.answer("Ошибка: файл meme.jpg не найден в папке с ботом!")


# --- Получение File ID от пользователя ---
@dp.message(F.photo)
async def get_file_id(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"Секретный код этого файла получен:\n{file_id}")


# --- Отправка по File ID ---
@dp.message(Command("show_id"))
async def show_by_id(message: types.Message):
    # Сюда нужно вставить реальный ID, который выдал бот
    saved_file_id = "AgACAgIAAxkBAAI..."
    await message.answer_photo(
        photo=saved_file_id,
        caption="Это фото отправлено по ID!"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())