# Такси_процедура
def taxi(distanse):
    base_tarif = 4
    float_tarif = 0.25
    return base_tarif + float_tarif*distanse*7.14

# Основная программа
distanse = float(input('Введите расстояние поездки (км): '))
print('Стоимость поездки %.2f' %taxi(distanse))