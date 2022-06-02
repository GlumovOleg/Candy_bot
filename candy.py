import settings
import telebot
import candyes

bot = telebot.TeleBot(settings.bot_token)

@bot.message_handler(['candy'])
def init_candy(message):
    bot.send_message(message.chat.id, candyes.start_game(message) , parse_mode='html')
    
@bot.message_handler()
def input_candy(message):
    bot.send_message(message.chat.id, candyes.game(message) , parse_mode='html')
    
bot.polling(non_stop=True)