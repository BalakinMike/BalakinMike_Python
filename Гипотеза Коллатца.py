chislo=int(input('Введите целое положительное число: '))
ch=chislo
print(ch)
while ch!=1:
    if ch%2==0:
        ch=ch//2
        chislo=chislo+ch
    else:
        ch=ch*3+1
        chislo=chislo+ch
    print(ch)
