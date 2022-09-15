# Пифагор_процедура
import math
def pifagor (a, b):
    c = math.sqrt(a**2 + b**2)
    return c

a = float(input('Введите катет а: '))
b = float(input('Введите катет b: '))
print('Гипотенуза равна %.2f' %pifagor (a, b))