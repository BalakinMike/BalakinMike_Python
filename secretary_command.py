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

def add_shell(append_dir):
    for key in directories.keys():
        if key == append_dir:
            directories[key].append(append_docs['number'])

def add():
    append_docs = {}
    append_docs['type'] = input('Введите тип документа (passport, invoice, insurance): ')
    append_docs['number'] = input('Введите номер документа в формате (passport: 0000 000000, invoice: 00-0, insurance: 00000): ')
    append_docs['name'] = input('Введите имя: ')
    append_dir = input('Введите номер полки для документа: ')
    documents.append(append_docs)
    
    if append_dir in directories:
        add_shell(append_dir)
    else:
        confirm = input('Введённой полки не существует. Создать новую полку? (д/н): ')
        if confirm == 'н':
            append_dir = (input('Введите правильный номер полки для документа: '))
            add_shell(append_dir)
        else:
            directories[n] = [append_docs['number']]

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
  
numbers = input('Введите номер документа: ')
while choice_doc(numbers) == None:
    print ('Введен несуществующий номер документа')
    numbers = input('Введите номер документа: ')
print('Владелец документа с номером ', numbers, choice_doc(numbers))

numbers = input('Введите номер документа: ')
while shell(numbers) == None:
    print ('Введен несуществующий номер документа')
    numbers = input('Введите номер документа: ')
print('Документ с номером ', numbers, 'находится на полке', shell(numbers))

list()