from aiogram import Router, types
from aiogram.filters.command import Command
import bot_text as bot_text
from utils.logger import logger

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} вызвал /start")
    await message.answer(bot_text.START_MESSAGE.format(name=message.from_user.first_name))