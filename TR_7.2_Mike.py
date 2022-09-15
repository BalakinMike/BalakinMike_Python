# Множества и подмножества

number_test = int(input('Введите количество тестовых случаев: '))
num=[]
ryad=[]
ryad_1=[]
ryad_2=[]
ryad_0=[] #список для суммирования двух введённых списков
mnoj=[]
for i in range (1,number_test):
    for j in range(0,2):
        print('Введите количество элементов', j+1, '- го множества:')
        num.append(int(input('')))
        print('Введите', j+1, '- ю строку элементов: ')
        s=input ('')
        for k in s:
            if k!=' ':
                ryad.append(k)
        ryad_1.append(ryad)
        print(ryad_1[j])
     #ryad_0=ryad_1[0]+ryad_1[1]
     #print(ryad_0)



      #  mnoj.append (set(ryad[j]))# преобразуем введённую строку в множество
       # print(len(mnoj[j]))
    
