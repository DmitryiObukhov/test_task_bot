from aiogram import types
from keyboards import locations_keyboard


async def send_welcome(message: types.Message):
    await message.answer(
        "Привіт! Це бот для обліку стану локацій. " "Будь ласка, оберіть локацію:",
        reply_markup=locations_keyboard,
    )
