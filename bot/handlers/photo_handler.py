from aiogram import types
from dotenv import load_dotenv
from openai_analysis import process_and_send_analysis
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def process_photo(bot, message, user_data, current_user):
    if current_user is not None:
        photo_file_id = message.photo[-1].file_id
        file_info = await bot.get_file(photo_file_id)
        file_path = file_info.file_path
        photo_link = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_path}"
        user_data[current_user]["photo_link"] = photo_link
        await message.answer("Фотографію збережено. Дякую за участь! Формую звіт...")
        await message.answer(f"Посилання на фотографію: {photo_link}")
        await process_and_send_analysis(
            bot,
            current_user,
            user_data[current_user]["location"],
            user_data[current_user]["checklist"],
        )
        clear_user_data(current_user)
        current_user = None
    else:
        await message.answer(
            "Спочатку введіть коментар, а потім завантажте фотографію."
        )
