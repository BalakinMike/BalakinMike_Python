fr=input('Введите слово: ')
fraza=fr.lower()
slovo=''
for j in fraza:
    if (j!=" "):
        slovo=slovo+j
print(slovo)
l=len(slovo)
n=0
i=-1
pal=True
while n<l/2:
    if slovo[n]!=slovo[i]:
        pal=False
    n=n+1
    i=i-1
if pal:
    print('Данное слово - палиндром')
else:
    print('Данное слово НЕ палиндром')