# Преобразрвание двоичного числа в десятичное
binar_num = input("Введите двоичное число: ")
n = len(binar_num)
j = -1  # Счётчик обратного счёта для введенного двоичного слова
m = 0  # Степень двойки
dec_num = 0  # Заготовка для десятичного числа
for i in range(n):
    dec_num = dec_num + (2**m * int(binar_num[j]))  #
    m = m + 1
    j = j - 1
print(dec_num)
