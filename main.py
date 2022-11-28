from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

from wiki import search_wiki

TOKEN = ""


def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['хаааай', 'приветики']:
        txt = "И тебе привет, друг!"

    update.message.reply_text(txt)


def start(update, context):
    update.message.reply_text("Это учебный зхобот.\nДля вызова помощи наберите /help")


def help(update, context):
    update.message.reply_text("Для поиска в википедии наберите /wiki <текст для поиска>")

def wikiword(update, context):
    print(context.args)
    word = " ".join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        result, url = search_wiki(word)
        update.message.reply_text(result+url)
    else:
        update.message.reply_text("Введите текст для поиска")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен...")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wiki", wikiword))

    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()