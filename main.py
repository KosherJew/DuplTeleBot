import telebot;
bot = telebot.TeleBot('2136905538:AAFK1Z3kCgHGj7PFKHeZvumrKOQiKXQdbG8')
@bot.message_handler()
def get_text_messages(message):
    bot.send_message(message.from_user.id,message.text)
bot.polling(none_stop=True, interval=0)