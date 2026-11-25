import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import echo, media
from utils.logger import logger
from handlers import start

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    logger.info("🚀 Запуск бота...")

    # Порядок важен: сначала точные, потом эхо
    dp.include_router(start.router)   # /start
    dp.include_router(media.router)   # /photo + стикеры
    dp.include_router(echo.router)    # приветствия + эхо (последним!)

    logger.info("✅ Все обработчики зарегистрированы")
    logger.info("🤖 Бот запущен и слушает сообщения...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())