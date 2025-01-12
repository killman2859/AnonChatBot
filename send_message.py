import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7357384085:AAHLCuyc9bbnqpMITA8TlJhr9cG9SzirvKg")


async def send_message(user_id, text):
    await bot.send_message(user_id, "")

send_message(1608921476, "А кто спрашивает?")