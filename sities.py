# Фильтрование списка визитов
geo_logs = [
    {"visit1": ["Москва", "Россия"]},
    {"visit2": ["Дели", "Индия"]},
    {"visit3": ["Владимир", "Россия"]},
    {"visit4": ["Лиссабон", "Португалия"]},
    {"visit5": ["Париж", "Франция"]},
    {"visit6": ["Лиссабон", "Португалия"]},
    {"visit7": ["Тула", "Россия"]},
    {"visit8": ["Тула", "Россия"]},
    {"visit9": ["Курск", "Россия"]},
    {"visit10": ["Архангельск", "Россия"]},
]

geo_logs_Rus = {}
for visit in geo_logs:
    for key in visit.values():
        for j in key:
            if j == "Россия":
                geo_logs_Rus = {**geo_logs_Rus, **visit}

print(geo_logs_Rus)
