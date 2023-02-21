import logging
import telegram
from telegram.ext import Application, ContextTypes, CommandHandler, MessageHandler, filters
import random

TOKEN = '6297686341:AAEdPRUcB7UgYg8PBEVxSpIe6i0KYAQ_Zik'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO 
)

async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='https://github.com/777414/cob_bot_tutorial')

async def echo(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Не понимаб')

if __name__ == '__main__':
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT or (~filters.COMMAND), echo))
    application.run_polling()
