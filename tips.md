message.from_user.first_name - возвращает имя пользователя 
F.text.lower() == "привет" - принимает конкретное слово
await message.reply - возвращает ответ как пересланное сообщение
user_name - имя пользователя



атрибуты для message:
•	text — буквы и цифры.
•	photo — информация об изображении.
•	sticker — данные о наклейке.


то есть, 
@dp.message(F.sticker) - принимает конкретно стикер
async def sticker_handler(message:types.Message):
    await message.answer_sticker(message.sticker.file_id) # отправляет стикер назад
    await message.answer(f"Я сохранил паспортный номер этого стикера: {message.sticker.file_id}")



await message.answer_photo - отвечает фоткой
await message.answer_sticker - отвечает стикером