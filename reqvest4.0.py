queries = [  # База запросов
    "смотреть сериалы онлайн",
    "новости спорта, политики,     экономика и бизнеса найти ",
    "афиша кино",
    "курс   доллара ",
    "сериалы этим летом    ",
    "курс по питону",
    "сериалы про спорт ",
    "кино  ",
    "как попасть в IT сферу "]
counter = {} 
for req in queries:
    counter[len(req. split())] = counter.get(len(req. split()), 0) + 1
#    print(counter)
for words, count in counter.items():
     print(f' из {words} слов {count/len(queries)*100}% ')