# Медиана трёх чисел
def mediana (a, b, c):
    media = a + b + c - max(a,b,c) - min(a,b,c)
    return media

# Основная программа
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
result_media = mediana (x,y,z)
print('Медиана введенных чисел равна ', result_media)