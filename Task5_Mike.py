Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
spisok=[] #Список слов
def sorti (spisok, lettr):# Подпрограмма выбора слов с буквой
  n=0
  for word in spisok:
    if lettr in word:
      n=n+1
  print('Число слов с буквой', lettr, '=', n)
run=True
while run:
  lett=input('Введите слово: ')
  if lett != 'стоп':
    spisok.append(lett)
  else:
    print('Конец набора')
    break
print('Производим подсчёт слов с заданной буквой. Для окончания работы нажмите "?"')
while run==True:
  lettr=input('Введите букву для выбора: ')
  if lettr!= "?":
    sorti(spisok,lettr)
  else: 
    run=False
