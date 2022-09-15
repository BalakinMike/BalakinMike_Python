x=float(input('Введите число: '))
guess=x/2
while (abs(guess*guess-x)>1e-12):
    guess=(guess+(x/guess))/2
print('sqq = ', guess)