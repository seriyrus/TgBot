from aiogram import Router, F
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import os
import psutil
import signal




start_router = Router()

def ease_link_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Выключить пк", callback_data = 'shutdown')],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Шпионим за Олегом!!!", reply_markup = ease_link_kb())

@start_router.callback_query(F.data == "shutdown")
async def shutdown_pk(callback_query: CallbackQuery):
    await os.system('shutdown -s /t 0')
    
    
@start_router.message(Command("check"))
async def check_tasks(message: Message):
    current_username = psutil.Process(os.getpid()).username()
    tasks = ""
    for proc in psutil.process_iter(['pid', 'username', 'name']):
        if proc.info['username'] == current_username:
            tasks += f"PID: {proc.info['pid']}, Имя: {proc.info['name']}\n"
    await message.answer(tasks)        
    
@start_router.message(Command("kill"))
async def cmd_settimer(
        message: Message,
        command: CommandObject
):
    # Если не переданы никакие аргументы, то
    # command.args будет None
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы"
        )
        return
    # Пробуем разделить аргументы на две части по первому встречному пробелу
    try:
        for proc in psutil.process_iter(['name']):
            if proc.info['name'] == command.args:
                try:
                    proc.kill()
                    print(f"Process '{proc.info['name']}' with PID {proc.pid} killed.")
                except psutil.NoSuchProcess:
                    print(f"Process with PID {proc.pid} already terminated.")
                except psutil.AccessDenied:
                    print(f"Access denied to kill process with PID {proc.pid}. Try running as administrator/root.")
                except Exception as e:
                    print(f"Error killing process with PID {proc.pid}: {e}")
    # Если получилось меньше двух частей, вылетит ValueError
    except ValueError:
        await message.answer(
            "Ошибка: неправильный формат команды. Пример:\n"
            "/settimer <time>"
        ) 
        return