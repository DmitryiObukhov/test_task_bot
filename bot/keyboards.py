from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

locations_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
locations_keyboard.add(KeyboardButton("Парк"))
locations_keyboard.add(KeyboardButton("Торгiвельний центр"))
locations_keyboard.add(KeyboardButton("Ресторан"))
locations_keyboard.add(KeyboardButton("Магазин"))
locations_keyboard.add(KeyboardButton("Проспект"))

checklist_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
checklist_keyboard.add(KeyboardButton("Все чисто"))
checklist_keyboard.add(KeyboardButton("Залишити коментар"))
checklist_keyboard.add(KeyboardButton("Аварiя"))
checklist_keyboard.add(KeyboardButton("Концерт"))
checklist_keyboard.add(KeyboardButton("Все добре"))
