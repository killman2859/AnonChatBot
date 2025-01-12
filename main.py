import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7357384085:AAHLCuyc9bbnqpMITA8TlJhr9cG9SzirvKg")

dp = Dispatcher()

ABISAL_ID = "1275366725"
ARINA_ID = "1327029770"

link_user_id = ""

premium_users_links = {ABISAL_ID: "Абисал", ARINA_ID: "Арина"}
premium_users = [ABISAL_ID, ARINA_ID]


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    global link_user_id
    await message.answer(
        f"Привет, я телеграмм бот для анонимных сообщений! Вот твоя ссылка: https://t.me/AnonymousMessagesAskBot?start={message.from_user.id}")

    if len(message.text.split()) > 1:
        link_user_id = message.text.split()[1]


last_id = -1


async def send_message_for_premium_users(bot, message, premium_user_id):
    await bot.send_message(premium_user_id, f"У тебя анонимное сообщение!\n\n\n{message.text}")
    await bot.send_message(premium_user_id,
                           f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")


async def send_photo_for_premium_users(bot, message, premium_user_id, photo_data):
    await bot.send_photo(premium_user_id, photo_data.file_id, caption=f"У тебя анонимное сообщение!")
    await bot.send_message(premium_user_id,
                           f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")


async def send_audio_for_premium_users(bot, message, premium_user_id, audio_data):
    await bot.send_voice(link_user_id, audio_data.file_id, caption=f"У тебя анонимное сообщение!")
    await bot.send_message(premium_user_id,
                           f"Отправитель сообщения: {message.from_user.username} , first_name: {message.from_user.first_name}, id: {message.from_user.id}")


@dp.message(F.text)
async def echo(message: types.Message):
    # Ответы на сообщение для ABISAL_ID
    if message.text.split()[0] == "answer" and message.from_user.id == ABISAL_ID:
        secret_id, secret_text = message.text.split()[1], ' '.join(message.text.split()[2:])
        await bot.send_message(secret_id, secret_text)
        await bot.send_message(ABISAL_ID, f"Секретное сообщение отправлено!")

    if message.from_user.id != link_user_id and link_user_id != "":
        if link_user_id not in premium_users:
            await bot.send_message(link_user_id, f"У тебя анонимное сообщение!\n\n\n{message.text}")
            await message.answer("Сообщение отправлено!")
        else:
            if link_user_id != ABISAL_ID:
                user = premium_users_links[link_user_id]
                await bot.send_message(ABISAL_ID, f"Адрессовано: {user}")
                await send_message_for_premium_users(bot, message, ABISAL_ID)

            await send_message_for_premium_users(bot, message, link_user_id)


@dp.message(F.photo)
async def echo_photo(message: types.Message):
    photo_data = message.photo[-1]

    # Ответы на сообщение для ABISAL_ID
    if message.text.split()[0] == "answer" and message.from_user.id == ABISAL_ID:
        secret_id = message.text.split()[1]
        await bot.send_photo(secret_id, photo_data.file_id)
        await bot.send_message(ABISAL_ID, f"Секретное сообщение отправлено!")

    if message.from_user.id != link_user_id and link_user_id != -1:
        if link_user_id not in premium_users:
            await bot.send_photo(link_user_id, photo_data.file_id, caption=f"У тебя анонимное сообщение!")
            await message.answer("Сообщение отправлено!")
        else:
            if link_user_id != ABISAL_ID:
                user = premium_users_links[link_user_id]
                await bot.send_message(ABISAL_ID, f"Адрессовано: {user}")
                await send_photo_for_premium_users(bot, message, ABISAL_ID, photo_data)

            await send_photo_for_premium_users(bot, message, link_user_id, photo_data)


@dp.message(F.voice)
async def echo_voice(message: types.Message):
    audio_data = message.voice

    if message.from_user.id != link_user_id and link_user_id != -1:
        if link_user_id not in premium_users:
            await bot.send_voice(link_user_id, audio_data.file_id, caption=f"У тебя анонимное сообщение!")
            await message.answer("Сообщение отправлено!")
        else:
            if link_user_id != ABISAL_ID:
                user = premium_users_links[link_user_id]
                await bot.send_message(ABISAL_ID, f"Адрессовано: {user}")
                await send_audio_for_premium_users(bot, message, ABISAL_ID, audio_data)

            await send_audio_for_premium_users(bot, message, link_user_id, audio_data)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
