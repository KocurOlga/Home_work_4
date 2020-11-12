string = """name:Иван
name:Петр
name:Марья
name:Дарья
name:Юля"""

#разделяем строку по переносам строки
string_elements = string.split('\n')

#задаем пустой список
user_list = []
#разделяем элементы по ':"
for elements in string_elements:
    words = elements.split(':')
    user_list.append(words[1])

print(user_list)
