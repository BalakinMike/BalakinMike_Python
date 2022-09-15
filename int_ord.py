# Числительные_процедура
def intToOrd(a):
    if a == 1:
        return 'first'
    elif a == 2:
        return 'second'
    elif a == 3:
        return 'third'
    elif a == 4:
        return 'fourth'
    elif a == 5:
        return 'fifth'
    elif a == 6:
        return 'sixth'
    elif a == 7:
        return 'seventh'
    elif a == 8:
        return 'eigth'
    elif a == 9:
        return 'ninth'
    elif a == 10:
        return 'tenth'
    elif a == 11:
        return 'eleventh'
    elif a == 12:
        return 'twelfth'
# Основная программа
if __name__ == '_main_':
    main()
for i in range (1,13):
    print(intToOrd(i))