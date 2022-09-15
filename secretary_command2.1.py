def choice_doc(numbers):
    for types in documents:
        for value in types.values():
            if value == numbers:
                return (types.get('name'))
        
def shell(numbers):
    for keys in directories:
        for value in range(0,len(directories[keys])):
            if numbers == directories[keys][value]:
                return (keys)

def list():
    for types in documents:
        print(types.get('type'), types.get('number'),types.get('name'))

def add():
    append_docs = {}
    append_docs['type'] = input('Введите тип документа (passport, invoice, insurance): ')
    append_docs['number'] = input('Введите номер документа в формате (passport: 0000 000000, invoice: 00-0, insurance: 00000): ')
    append_docs['name'] = input('Введите имя: ')
    append_dir = input('Введите номер полки для документа: ')
    documents.append(append_docs)
    
    if append_dir in directories:
        for key in directories.keys():
            if key == append_dir:
                directories[key].append(append_docs['number'])
    else:
        confirm = input('Введённой полки не существует. Создать новую полку? (д/н): ')
        if confirm == 'н':
            append_dir = (input('Введите правильный номер полки для документа: '))
            for key in directories.keys():
                if key == append_dir:
                    directories[key].append(append_docs['number'])
        else:
            directories[append_dir] = [append_docs['number']]

def commanda_base(commanda):
    if commanda == 'p':  
        numbers = input('Введите номер документа: ')
        while choice_doc(numbers) == None:
            print ('Введен несуществующий номер документа')
            numbers = input('Введите номер документа: ')
        print('Владелец документа с номером ', numbers, choice_doc(numbers))
    elif commanda == 's':
        numbers = input('Введите номер документа: ')
        while shell(numbers) == None:
            print ('Введен несуществующий номер документа')
            numbers = input('Введите номер документа: ')
        print('Документ с номером ', numbers, 'находится на полке', shell(numbers))
    elif commanda == 'l':
        list()
    elif commanda == 'a':
        add()

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Пупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Крокодил Геннадий'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Чебуранов'}
  ]

directories = {
    '1': ['2207 876234', '11-2', '5545 028765'],
    '2': ['10006'],
    '3': []
  }

# Основная программа
print('p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
print('s – команда, выведет номер полки, на которой находится документ')
print('l – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
print('a – команда, которая добавит новый документ в каталог и в перечень полок.')
commanda = ''
while commanda != 'exit':
    while commanda != 'p' and commanda != 's' and commanda != 'l' and commanda != 'a':
        commanda = input('Введите команду (p, s, l, a): ')
        commanda_base(commanda)
    