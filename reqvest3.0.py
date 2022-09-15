# Найти количество слов в запросе
def amount(reqvest):
    while reqvest[-1:] == ' ':
        reqvest = reqvest[:-1]
    n = 0  # Счётчик количества слов
    space = '' 
    for i in reqvest:
        if i == " " and space != ' ':  # Слово, если найден пробел
            n = n + 1
            space = ' ' # Защита от лишних пробелов внутри строки
        if i != ' ' and space == ' ':
          space = ''
    return n + 1 # Учёт последнего слова


queries = [  # База запросов
    "смотреть сериалы онлайн",
    "новости спорта, политики,     экономика и бизнеса найти ",
    "афиша кино",
    "курс   доллара ",
    "сериалы этим летом    ",
    "курс по питону",
    "сериалы про спорт ",
    "кино  ",
    "как попасть в IT сферу "
]

sum_reqvest = len(queries)  # Общее количество запросов
friqvency = [] # Формирование списка количества слов в запросах
for j in queries:
    friqvency.append(amount(j))

number_req = 0 # Вспомогательный (накопительный) счётчик количества запросов 
i = 1 # Счётчик числа слов в запросе
while number_req != sum_reqvest: # Пока вспомогательный счётчик меньше количества запросов ...
    number_req = number_req + 1
    if friqvency.count(i) != 0:
        print('Запросов, содержащих ', i, 'слов %.2f' % ((friqvency.count(i)/sum_reqvest)*100), '%')
    i = i + 1






