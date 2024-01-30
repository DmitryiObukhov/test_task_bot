from aiogram import types
from keyboards import checklist_keyboard


async def choose_location(message: types.Message, **kwargs):
    user_data = kwargs.get("user_data", None)

    if user_data is not None:
        location = message.text
        user_data[message.chat.id] = {"location": location, "checklist": {}}
        await message.answer(
            f"Ви обрали {location}. Тепер оберіть пункт чек-листу:",
            reply_markup=checklist_keyboard,
        )
    else:
        print("user_data is None. Please check if it's passed correctly.")
