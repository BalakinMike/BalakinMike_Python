n=int(input('Введите число - предел создания таблицы: '))
for i in range (1,n+1):
    print(' ','{:>3d}'.format(i), end='') #Форматирование отводит 3 знака под целое число и выравнивает по правому краю
print('')
for i in range (1,n+1):
    print('{:>2d}'.format(i), end='')
    for j in range (1,n+1):
        print('{:>3d}'.format(i*j),' ', end='')
    print('')