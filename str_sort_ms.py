#input_string=input()
input_string="Processsing sorting Of strange string qXbt56^fk! and alittle bit more sssssssssSSSSss and ooOooOoo"
#
# Lets' create a dictionary {char:number}
char_number_dict={}
for char in input_string.lower():               # transfer string to lowercase
    if char.isalpha():                          # we don't need other characters - like numbers or punctuations
        char_number_dict.setdefault(char,0)     # number is 0 by default; if char already exists - do nothing; можно через get() проверять на None еще
        char_number_dict[char] += 1
#	
print (char_number_dict)
# Result:
# {'p': 1, 'r': 5, 'o': 12, 'c': 1, 'e': 4, 's': 21, 'i': 5, 'n': 6, 'g': 4, 't': 7, 'f': 2, 'a': 4, 'q': 1, 'x': 1, 'b': 2, 'k': 1, 'd': 2, 'l': 2, 'm': 1}
#####################################################################
# Approach #1
# Let's sort the dictionary by key (it supposed that we are using Python >3.7)
sorted_char = {}
for key in sorted(char_number_dict):
    sorted_char[key]=char_number_dict[key]
#    
print(sorted_char)
# Result:
# {'a': 4, 'b': 2, 'c': 1, 'd': 2, 'e': 4, 'f': 2, 'g': 4, 'i': 5, 'k': 1, 'l': 2, 'm': 1, 'n': 6, 'o': 12, 'p': 1, 'q': 1, 'r': 5, 's': 21, 't': 7, 'x': 1}
#
value_list = list(sorted_char.values())
value_list.sort(reverse=True)
print(value_list)
# Result:
# [21, 12, 7, 6, 5, 5, 4, 4, 4, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
previous_number = -1
res_dict={}
for number in value_list:
    if number == previous_number:
        continue                            # to avoid the dublicats (разные символы могут встретится одинаковое число раз - например -a,e,g в моей строке)
    for char in sorted_char:
        if sorted_char[char] == number:
            res_dict[char]=number
print(res_dict)            
# Result:
# {'s': 21, 'o': 12, 't': 7, 'n': 6, 'i': 5, 'r': 5, 'a': 4, 'e': 4, 'g': 4, 'b': 2, 'd': 2, 'f': 2, 'l': 2, 'c': 1, 'k': 1, 'm': 1, 'p': 1, 'q': 1, 'x': 1}
#####################################################################
# Approach #2
# Let's build a dictionary {number: [list of characters]}
number_charlist_dict = {}
for key,val in char_number_dict.items():
    number_charlist_dict.setdefault(val,[])
    number_charlist_dict[val].append(key)
print(number_charlist_dict)    
# Result:
# {1: ['p', 'c', 'q', 'x', 'k', 'm'], 5: ['r', 'i'], 12: ['o'], 4: ['e', 'g', 'a'], 21: ['s'], 6: ['n'], 7: ['t'], 2: ['f', 'b', 'd', 'l']}
sorted_numchar_dict = {}
num_list = list(number_charlist_dict.keys())
num_list.sort(reverse=True)
for num in num_list:
    sorted_numchar_dict[num] = number_charlist_dict[num]
print(sorted_numchar_dict)    
# Result:
# {21: ['s'], 12: ['o'], 7: ['t'], 6: ['n'], 5: ['r', 'i'], 4: ['e', 'g', 'a'], 2: ['f', 'b', 'd', 'l'], 1: ['p', 'c', 'q', 'x', 'k', 'm']}
res_dict = {}
for num in sorted_numchar_dict.keys():
    char_list = sorted_numchar_dict[num]
    char_list.sort()
    for char in char_list:
        res_dict[char] = num
print(res_dict)
# Result:
# {'s': 21, 'o': 12, 't': 7, 'n': 6, 'i': 5, 'r': 5, 'a': 4, 'e': 4, 'g': 4, 'b': 2, 'd': 2, 'f': 2, 'l': 2, 'c': 1, 'k': 1, 'm': 1, 'p': 1, 'q': 1, 'x': 1}
#####################################################################
# Approach #3
res_dict = dict(sorted(char_number_dict.items(), key=lambda item: (-item[1], item[0])))
print (res_dict)
# Result:
# {'s': 21, 'o': 12, 't': 7, 'n': 6, 'i': 5, 'r': 5, 'a': 4, 'e': 4, 'g': 4, 'b': 2, 'd': 2, 'f': 2, 'l': 2, 'c': 1, 'k': 1, 'm': 1, 'p': 1, 'q': 1, 'x': 1}
# хорошее, но длинное объяснение, как эта магия работает, здесь: https://davidbpython.com/advanced_python/slides/handout-43-3.html
# Кратко:
# char_number_dict.items() - это массив пар символ:число
# dict_items([('p', 1), ('r', 5), ('o', 12), ('c', 1), ('e', 4), ('s', 21), ('i', 5), ('n', 6), ('g', 4), ('t', 7), ('f', 2), ('a', 4), ('q', 1), ('x', 1), ('b', 2), ('k', 1), ('d', 2), ('l', 2), ('m', 1)])
# далее мы это дело сортируем с помощью функции соавнения: метод sorted в Питоне может иметь три параметра - что сортировать, как (с помощью какой функции сравнения и reverse - да/нет. У нас функция сравнения:
# (-item[1], item[0])
# таким образом мы говорим компу, что в первую очередь надо сортировать по элементу №1 в паре (кол-во таких символов в строке) - но, поскольку он с минусом,то делать это в обратном порядке - по убыванию. 
# А если сравнение по первому элементу дает одинаковый результат для двух пар, то сравнивать элемент №0 (символ). Он без минуса, так что - по возрастанию
# Возможно, что более понятен будет такой код:
#
def sort_function(key):
    return -char_number_dict[key]*1000+(ord(key))
# Это функция, которую я придумал для сравнения элементов словаря. Более важный элемент - value = кол-во раз, которое символ встречается. Чтобы сделать его более важным, я его умнгожил на 1000. Но - для того, чтобы сортирвка шла в обратном порядке, а не как стандартно в Питоне (по возрастанию) - я его использую с минусом
# Но, для того, чтобы в сравнении участвовал еще и сам символ (если номера одинаковы - я добавляю в результат функции сравнения порядковый номер симовола.
sorted_char_list = sorted(char_number_dict, key=sort_function)
print(sorted_char_list)
# Result:
# ['s', 'o', 't', 'n', 'i', 'r', 'a', 'e', 'g', 'b', 'd', 'f', 'l', 'c', 'k', 'm', 'p', 'q', 'x']
res_dict = {}
for char in sorted_char_list:
    res_dict[char] = char_number_dict[char]
print(res_dict)
# Result:
# {'s': 21, 'o': 12, 't': 7, 'n': 6, 'i': 5, 'r': 5, 'a': 4, 'e': 4, 'g': 4, 'b': 2, 'd': 2, 'f': 2, 'l': 2, 'c': 1, 'k': 1, 'm': 1, 'p': 1, 'q': 1, 'x': 1}
# То-же самое, но в предыдущем решении - просто более компактная запись. Но и более непонятная - для меня. Но я Питон, как выяснилось - основательно подзабыл    