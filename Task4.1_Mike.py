Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
help="""Справка по программе:
help - вывести справку по программе
add - добавить задачу в список (название задачи запрашиваем у пользователя)
show - показать список задач
exit - окончание работы"""
today=[]
tomorrow=[]
tasks= []
run=True
while run:
  command = input ('Введите команду: ')
  if command == "help":
    print (help)
  elif command == "show":
    print ('Сегодня:', today, 'Завтра:', tomorrow, 'Прочие', tasks)
  elif command =="add":
    date=input('Введите дату: ')
    task=input('Введите задачу: ')
    if date=='Сегодня':
      today.append(task)
    elif date=='Завтра':
      tomorrow.append(task)
    else:
      tasks.append(task)
    print('Задача добавлена')
  elif command=="exit":
    print('Спасибо за использование! До свидания!')
    run=False
  else: 
    print('Неизвестная команда')
