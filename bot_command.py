from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler
import log

async def help(update, context):    
    await update.message.reply_text(f'/game\n/help')
    f = open('db.csv', 'a')
    f.write(f'{update.message.text} {update.effective_user.first_name} {update.effective_user.id}\n')
    f.close()
    
async def game(update, context):    
    await context.bot.send_message(chat_id=update.effective_chat.id, 
                                   text="Я бот, делаю возведение в квадрат за деньги! Напишите вашу цифру для расчета: ")   
    f = open('db.csv', 'a')
    f.write(f'{update.message.text} {update.effective_user.first_name} {update.effective_user.id}\n')
    f.close()

async def quadr(update, context):
    digit = update.message.text
    res = int(digit[0]) ** 2
    f = open('db.csv', 'a')
    f.write(f'{update.message.text} {update.effective_user.first_name} {update.effective_user.id}\n')
    f.close()  
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Результат вычисления - {res}, {update.effective_user.first_name}, с Вас 1 000 000 $, средства будут списаны с вашей карты в течение 5 секунд" )    


       
    
    
    

