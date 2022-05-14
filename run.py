import logging
from pymongo import MongoClient
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, CallbackContext


from db import operations


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

client = MongoClient('localhost', 27017)
db = client['gng-wallet-bot']

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if operations.create_user(db, chat_id):
        await context.bot.send_message(chat_id=chat_id, text="Welcome!")

async def info(update: Update, context: CallbackContext.DEFAULT_TYPE):
    user = operations.get_user(db, update.effective_chat.id)
    if user:
        text = user.info()
        await context.bot.send_message(chat_id=user.chat_id, text=text)

if __name__ == '__main__':
    application = ApplicationBuilder().token('5344910771:AAE_TrMWYaxNspvxM0gkhXLVM8FkbMzbtk4').build()

    start_handler = CommandHandler('start', start)
    info_handler = CommandHandler('info', info)

    application.add_handler(start_handler)
    application.add_handler(info_handler)

    application.run_polling()
