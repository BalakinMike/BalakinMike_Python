Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import telebot
token = '5121462939:AAGGAnCPm7ymYZHwBeLn33rEb2Bt5JiUMj8'
bot=telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)
bot.polling(non_stop=True)
