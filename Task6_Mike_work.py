Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import telebot
import random

token = '5121462939:AAGGAnCPm7ymYZHwBeLn33rEb2Bt5JiUMj8'
bot=telebot.TeleBot(token)

help = """Справка по программе:
/help - вывести справку по программе
/add - добавить задачу в список (название задачи запрашиваем у пользователя)
/show - показать список задач
/exit - окончание работы
/random - добавлять случайную задачу на дату Сегодня """

random_tasks = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]
tasks = {}

def todo (date, task):
    if date in tasks:
      tasks[date].append(task)
    else:
      tasks[date]=[]
      tasks[date].append(task)


@bot.message_handler(commands=['help'])
def help(message):
      bot.send_message(message.chat.id,help)

@bot.message_handler(commands=['add'])
def add(message):
    command=message.text.split(maxsplit=2)
    date=command[1].lower()
    task=command[2]
    todo(date, task)
    text= 'Задача '+ task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['random'])
def random_add(message):
    date='сегодня'
    task=random.choice(random_tasks)
    todo(date, task)
    text= 'Задача '+ task + ' добавлена на дату ' + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['show', 'print'])
def show(message):
    command=message.text.split(maxsplit=1)
    date = command[1].lower()
    text=""
    if date in tasks:
        text=date.upper()+'\n'
        for task in tasks[date]:
            text=text+'[]'+task+'\n'
    else:
        text='Задач на эту дату нет'
    bot.send_message(message.chat.id, text)

#обращение к Телеграмм
bot.polling(non_stop=True)