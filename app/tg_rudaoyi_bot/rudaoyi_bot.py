from telegram import Update,Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# app = ApplicationBuilder().token(my_token).build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()

my_token='8368171227:AAH_p0VsLie2vvch8clKZDqaaQeITJeyCaA'
chat_id=-1003452427824
bot = Bot(token=my_token)
async def send_message(text,bot=bot, chat_id=chat_id):
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == "__main__":
    asyncio.run(send_message("Hello from rudaoyi_bot!"))