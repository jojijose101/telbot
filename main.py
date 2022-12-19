import constant as keys
from telegram.ext import *
import Responses as R

print(" Bot started... ")

def start_command(update,context):
    update.message.reply_text('Type something random to get started!')

def help_command(update,context):
        update.message.reply_text('If you need help! You should ask for it on Google!')

def handle_message(update,context):
    text = str(update.message.text).lower()
    responses = R.sample_responses(text)

    update.message.reply_text(responses)
def error(update,context):
    print(f"update {update} caused error {context.error}")

updater = Updater(keys.API_KEY, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start",start_command))
dp.add_handler(CommandHandler("help",help_command))
dp.add_handler(MessageHandler(Filters.text, handle_message))

updater.start_polling()
updater.idle()


