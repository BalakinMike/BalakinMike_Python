Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random
help="""Справка по программе:
help - вывести справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - показать список задач
exit - окончание работы
random - добавлять случайную задачу на дату Сегодня """
random_tasks = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]
tasks= {}
def todo (date, task):
    if date in tasks:
      tasks[date].append(task)
    else:
      tasks[date]=[]
      tasks[date].append(task)
    print('На дату ', date, 'добавлена задача ', task)

run=True
while run:
  command = input ('Введите команду: ')
  if command == "help":
    print (help)
  elif command == "show":
    date=input('Введите дату искомой задачи: ')
    if date in tasks:
      for task in tasks[date]:
        print('-', task)
    else:
        print ('Такой даты нет')
  elif command =="add":
    date=input('Введите дату: ')
    task=input('Введите задачу: ')
    todo(date,task)
  elif command=="random":
    task=random.choice(random_tasks)
    todo("Сегодня",task)
  elif command=="exit":
    print('Спасибо за использование! До свидания!')
    run=False
  else: 
    print('Неизвестная команда')
