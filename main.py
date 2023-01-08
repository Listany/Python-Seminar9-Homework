from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, filters, MessageHandler
import bot_command
from config import TOKEN

application = ApplicationBuilder().token(TOKEN).build()
    
game_handler = CommandHandler('game', bot_command.game)
help_handler = CommandHandler('help', bot_command.help)
quadr_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), bot_command.quadr)    
    
application.add_handler(game_handler)
application.add_handler(quadr_handler)
application.add_handler(help_handler)
    
print('server run')
application.run_polling()