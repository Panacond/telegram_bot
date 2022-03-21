from telegram.ext import Updater
updater = Updater(token='BOT_TOKEN', use_context=True)

from telegram.ext import MessageHandler, Filters, CallbackContext

from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")