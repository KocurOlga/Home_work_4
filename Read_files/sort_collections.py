import collections


input_string = 'Москва слезам не верит'

# Создаем список из букв
letter_list = list(input_string)

# Создаем переменную letter_counter, используя объект Counter из модуля collections
# В объект Counter передаем список букв
letter_counter = collections.Counter(letter_list)

print(letter_counter) #({'b': 3, 'a': 2, 'c': 2, 'd': 1})
print(letter_counter.most_common(1)) #[('b', 3), ('a', 2), ('c', 2)]
print(letter_counter.most_common(1)[0][0]) #b
print(letter_counter.most_common(1)[0][1]) #3
