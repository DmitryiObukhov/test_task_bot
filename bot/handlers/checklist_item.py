from aiogram import types
from keyboards import checklist_keyboard


async def choose_checklist_item(message: types.Message, user_data):
    chat_id = message.chat.id

    if user_data[chat_id]["checklist"]:
        await message.answer("Результат вже збережено. Операцiя завершена.")
        return

    item = message.text

    if item in ["Все чисто", "Аварiя", "Концерт", "Все добре"]:
        user_data[chat_id]["checklist"][item] = None
        await message.answer(f"Ви обрали '{item}'. Результат збережено.")
        user_data[chat_id]["checklist_saved"] = True
    elif "Залишити коментар" in item:
        user_data[chat_id]["checklist"][item] = None
        await message.answer("Введіть ваш коментар:")
        user_data[chat_id]["checklist_saved"] = True
    else:
        await message.answer(f"Ви обрали {item}.", reply_markup=checklist_keyboard)
