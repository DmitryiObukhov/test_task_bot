from aiogram import Bot
import openai


async def process_and_send_analysis(bot, chat_id, location, checklist):
    input_text = f"Локацiя: {location}\nКоментар: {checklist}"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=input_text, max_tokens=150
        )
        analysis_result = response["choices"][0]["text"]
        await bot.send_message(chat_id, f"Звiт вiд OpenAI:\n{analysis_result}")
    except Exception as e:
        await bot.send_message(
            chat_id, f"Сталася помилка під час аналізу даних на OpenAI: {str(e)}"
        )
