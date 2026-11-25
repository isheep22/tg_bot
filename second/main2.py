import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.types import FSInputFile


load_dotenv()

# 1. ВКЛЮЧАЕМ ЖУРНАЛ СОБЫТИЙ (Логирование)
logging.basicConfig(level=logging.INFO)

# 2. СОЗДАЕМ ТЕЛО И МОЗГ
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Проверь файл .env")

bot = Bot(token=BOT_TOKEN) # Твое тело (выполняет приказы)
dp = Dispatcher()          # Твой мозг (принимает решения)





# 3. СТАВИМ ЛОВУШКУ (Хэндлер)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Бот печатает ответ
    await message.answer(f"Привет {message.from_user.first_name}! Готов к работе")
    
    
@dp.message(F.text.lower() == "привет")
@dp.message(F.text.lower() == "йоу") 
@dp.message(F.text.lower() == "здарова") 
@dp.message(F.text.lower() == "ку") 
async def hello_handler(message: types.Message):
    await message.reply("И тебе привет! Пока доступна команда: /start")


@dp.message(Command("photo"))
async def send_photo(message: types.Message):
    # 1. Указываем путь к файлу
    photo_file = FSInputFile("images/flower.jpg")

    # 2. Даем команду на отправку
    await message.answer_photo(
        photo=photo_file,
        caption="Лови мой любимый цветок 🐱"
    )



@dp.message(F.sticker) # - принимает конкретно стикер
async def sticker_handler(message:types.Message):
    await message.answer_sticker(message.sticker.file_id) # отправляет стикер назад
    await message.answer(f"Я сохранил паспортный номер этого стикера: {message.sticker.file_id}")

@dp.message(F.text)
async def cmd_start(message: types.Message):
    # Бот печатает ответ
    await message.answer(f"{message.text} 🦜")
    


# 4. ЗАПУСК ДВИГАТЕЛЯ
async def main():
    await dp.start_polling(bot)

# 5. КРАСНАЯ КНОПКА СТАРТА
if __name__ == "__main__":
    asyncio.run(main())




