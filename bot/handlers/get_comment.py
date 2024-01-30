from aiogram import types


async def get_comment(message: types.Message, user_data):
    comment = message.text
    chat_id = message.chat.id

    checklist_item = next(
        item for item in user_data[chat_id]["checklist"] if "Залишити коментар" in item
    )
    user_data[chat_id]["checklist"][checklist_item] = comment
    await message.answer("Коментар збережено. Завантажте фотографію:")
