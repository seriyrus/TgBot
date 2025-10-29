import asyncio
from Bot import bot, dp
from handlers.start import start_router, ease_link_kb

async def send_startup_message(bot: bot):
    """Отправляет приветственное сообщение пользователю при запуске."""
    await bot.send_message(1379922423, "Цель в сети!!!", reply_markup=ease_link_kb())
    await asyncio.sleep(1)

async def main():
    dp.include_router(start_router)
    dp.startup.register(send_startup_message)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    


if __name__ == "__main__":
    asyncio.run(main())