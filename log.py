from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    f = open('db.csv', 'a')
    f.write(f'{update.message.text}\n')
    f.close()