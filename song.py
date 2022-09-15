# Песня
from int_ord import intToOrd

def text_song(n):
    print('On the', intToOrd(n), 'day of Christmas')
    print('My true love send to me:')
    if n >= 12:
        print('Twelve drummers drumming,')
    if n >= 11:
        print("Eleven pipers piping,")
    if n >= 10:
        print("Ten lords a–leaping,")
    if n >= 9:
        print("Nine ladies dancing,")
    if n >= 8:
        print("Eight maids a–milking,")
    if n >= 7:
        print("Seven swans a–swimming,")
    if n >= 6:
        print("Six geese a–laying,")
    if n >= 5:
        print("Five golden rings,")
    if n >= 4:
        print("Four calling birds,")
    if n >= 3:
        print("Three French hens,")
    if n >= 2:
        print("Two turtle doves,")
    if n == 1:
        print("A", end=" ")
    else:
        print("And a", end=" ")
    print("partridge in a pear tree.")
    print()
# Основная программа
for i in range (1,13):
    text_song(i)