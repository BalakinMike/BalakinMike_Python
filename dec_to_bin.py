# Преобразование десятичного числа в двоичное
q = int(input("Введите целое десятичное число: "))
result = ""
while q != 0:
    r = q % 2
    result = str(r) + result
    q = q // 2
print(result)
