import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from open_api import img_gen

telegram_bot_token = 

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):#greeting on starting
    update.message.reply_text("Hey there! you have started chatting with Vbot\n here you can request any images!")
    update.message.reply_text("you can type something to get your AI image in 1080p")

def get_word_info(update, context):#creating the image fun call
    image=img_gen(update.message.text)

    update.message.reply_text(image)
    update.message.reply_text("YOUR DESIRED IMAGE IS HERE! DOWNLOAD IT FROM THE LINK IF THE IMAGE IS NOT LOADED!")
    update.message.reply_text("NOTICE:")
    update.message.reply_text("\n YOUR LINK WILL EXPIRE IN 1 HOUR")

 
dispatcher.add_handler(CommandHandler("start", start))#main fun starts
dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))

updater.start_polling()
