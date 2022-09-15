
def dayOFnumber(year,number_day):
    # Определяем високосность года
    if (year%100) == 0:
        if (year%400) == 0:
            vis_year = True
        else:
            vis_year = False
    elif (year%4) == 0:
        vis_year = True
    else:
        vis_year = False
    
    if vis_year: # Если год високосный
        if number_day <= 366:
            if number_day > 335:
                print ('декабрь', number_day - 335)
            elif number_day > 305:
                print ('ноябрь', number_day - 305)
            elif number_day > 274:
                print ('октябрь', number_day - 274)
            elif number_day > 243:
                print ('сентябрь', number_day - 243)
            elif number_day > 213:
                print ('август', number_day - 213)
            elif number_day > 182:
                print ('июль', number_day - 182)
            elif number_day > 151:
                print ('июнь', number_day - 151)
            elif number_day > 121:
                print ('май', number_day - 121)
            elif number_day > 90:
                print ('апрель', number_day - 90)
            elif number_day > 60:
                print ('март', number_day - 60)
            elif number_day > 31:
                print ('февраль', number_day - 31)
            else:
                print ('январь', number_day)
    else: # Если год невисокосный
        if number_day <= 365:
            if number_day > 334:
                print ('декабрь', number_day - 334)
            elif number_day > 304:
                print ('ноябрь', number_day - 304)
            elif number_day > 273:
                print ('октябрь', number_day - 273)
            elif number_day > 242:
                print ('сентябрь', number_day - 242)
            elif number_day > 212:
                print ('август', number_day - 212)
            elif number_day > 181:
                print ('июль', number_day - 181)
            elif number_day > 150:
                print ('июнь', number_day - 150)
            elif number_day > 120:
                print ('май', number_day - 120)
            elif number_day > 89:
                print ('апрель', number_day - 89)
            elif number_day > 59:
                print ('март', number_day - 59)
            elif number_day > 31:
                print ('февраль', number_day - 31)
            else:
                print ('январь', number_day)    

# Основная программа
year=int(input('Введите год: '))
number_day=int(input('Введите номер дня: '))
dayOFnumber(year,number_day)