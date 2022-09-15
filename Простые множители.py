# Простые множители
factor = 2
n = int(
    input("Введите целое число (2 или больше), простые множители к которому ищем: ")
)
while n < 2:
    print("Ошибка: Введено значение меньше 2.")
    n = int(
        input("Введите целое число (2 или больше), простые множители к которому ищем: ")
    )
while factor < n:
    if n % factor == 0:
        print(factor)
        n = n // factor
    else:
        factor = factor + 1
print(n)
