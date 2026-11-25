from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile
import bot_text
from utils.logger import logger

router = Router()

@router.message(Command("photo"))
async def send_photo(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} вызвал /photo")
    photo_file = FSInputFile("images/flower.jpg")
    await message.answer_photo(
        photo=photo_file,
        caption=bot_text.PHOTO_CAPTION
    )

@router.message(F.sticker)
async def sticker_handler(message: types.Message):
    logger.info(f"Пользователь {message.from_user.id} прислал стикер")
    await message.answer_sticker(message.sticker.file_id)
    await message.answer(bot_text.STICKER_SAVED.format(file_id=message.sticker.file_id))