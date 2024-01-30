from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv
from keyboards import locations_keyboard, checklist_keyboard
from handlers.send_welcome import send_welcome
from handlers.choose_location import choose_location
from handlers.checklist_item import choose_checklist_item
from handlers.get_comment import get_comment
from handlers.photo_handler import process_photo
import os
import openai
import logging

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("GPT_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

user_data = {}
current_user = None


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await send_welcome(message)


@dp.message_handler(
    lambda message: message.text
    in ["Парк", "Торгiвельний центр", "Ресторан", "Магазин", "Проспект"]
)
async def location_command(message: types.Message):
    await choose_location(message, user_data=user_data)


def clear_user_data(chat_id):
    user_data[chat_id]["checklist"] = {}


@dp.message_handler(
    lambda message: message.text
    in ["Все чисто", "Залишити коментар", "Аварiя", "Концерт", "Все добре"]
)
async def checklist_item_command(message: types.Message):
    await choose_checklist_item(message, user_data=user_data)


@dp.message_handler(
    lambda message: "Залишити коментар"
    in user_data[message.chat.id]["checklist"].keys()
)
async def get_comment_command(message: types.Message):
    global current_user
    current_user = message.chat.id
    await get_comment(message, user_data=user_data)


@dp.message_handler(content_types=["photo"])
async def get_photo(message: types.Message):
    global current_user
    await process_photo(bot, message, user_data, current_user)


dp.register_message_handler(checklist_item_command)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
