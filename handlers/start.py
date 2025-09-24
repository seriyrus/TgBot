from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

start_router = Router()

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Выключить пк", callback_data = 'shutdown')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Шпионим за Олегом!!!", reply_markup = ease_link_kb())

@start_router.message(Command('shutdown'))
async def shutdown_pk(message: Message):
    await os.command('shutdown -s /t 0')