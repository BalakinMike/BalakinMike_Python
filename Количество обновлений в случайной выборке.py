# Поиск числа обновлений максимума в случайной выборке из 100
from itertools import count
from random import randrange  #


num = randrange(1, 100, 1)  # Генерация случайного числа из 100 с шагом 1
max_num = num  # Объявляем первое число максимальным
count = 1
for i in range(1, 100):
    num = randrange(1, 100, 1)
    if max_num < num:
        max_num = num  # Обновляем максимальное число
        print(num, "<== обновление")
        count = count + 1  # Обновляем счётчик
    else:
        print(num)
print("Количество обновлений = ", count)
