import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "8689267726:AAEG7DR15ajxyigTDKvFnaomcsyUedJgR08"
ADMIN_ID =  7305807529

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот по скупке скинов CS2 🎮")

@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    print("Бот запущен! Ожидаю сообщения...")
    await dp.start_polling(bot)

if __name__== "__main__":
    asyncio.run(main())
