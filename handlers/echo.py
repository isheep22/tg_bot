from aiogram import Router, F, types
import bot_text
from utils.logger import logger

router = Router()

# Приветствия — в любом регистре (благодаря .lower())
@router.message(F.text.lower().in_({"привет", "йоу", "здарова", "ку"}))
async def hello_handler(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} поздоровался")
    await message.reply(bot_text.HELLO_MESSAGE)

# Эхо-заглушка — ловит всё остальное (регистрируется последним!)
@router.message(F.text)
async def echo_handler(message: types.Message):
    logger.info(f"Эхо от {message.from_user.id}: {message.text[:50]}")
    await message.answer(f"{message.text} 🦜")