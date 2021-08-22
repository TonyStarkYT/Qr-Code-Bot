import logging
import os
import png
from pyqrcode import QRCode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
TOKEN = os.environ.get('TOKEN')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

start_msg = '''
<b>HELLO THERE <b>👋👋
<i>Welcome TO Qr code generator Bot</i>
<i>Send Me any Email ID,Text,url,spotify song link etc I will generate a qr code for it</i>
<b>Direct Media files Are not supported</b>
<i>How ever U can send a direct link to those files</i>
<i>Creator :</i> [NxtStark](https://telegram.me/NxtStark)
'''
help_msg = '''
<i> Just Send me any Email Id,Text ,url etc(no media files...)</i>
<i>I will generate a Qr Code for it and send it to you</i>
'''
about_msg = '''
<b>Bot :</b> <i>Backround Remover Bot</i>
<i>Creator :</i> [NxtStark](https://telegram.me/NxtStark)
<i>Channel :</i> [HTechMedia](https://telegram.me/HTechMedia)
<i>Source :</i> [Click here](https://github.com/HTechMedia/Remove-BG-Bot/tree/main)
<i>Language :</i> [Python3](https://python.org)
<i>Library :</i> [Pyrogram](https://pyrogram.org)
<i>Server :</i> [Heroku](https://heroku.com)
'''

def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_html(start_msg)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_html(help_msg)
    
def about_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /about is issued."""
    update.message.reply_html(about_msg)    


def msg(update: Update, context: CallbackContext) -> None:
    """Send Any text or url to get a qr code for it"""
    text = update.message.text
    message_id = update.message.message_id
    qr_file = f'{message_id}.png'
    try:
        update.message.reply_text("Generating")
        Qr_Code = QRCode(text)
        Qr_Code.png(qr_file, scale=10)
        update.message.reply_photo(photo=open(
            qr_file, "rb"), reply_to_message_id=message_id, caption=f"Here is Your Qr code for '{text}'")
        update.message.reply_text("Finished")
        os.remove(qr_file)
    except Exception:
        update.message.reply_text("Please Try Agian Later")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, msg))
    # Start The bot
    
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
