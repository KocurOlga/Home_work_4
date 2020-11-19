from collections import defaultdict, Counter

sales_log = [{'user': 'Маша', 'item': 'Телескоп'},
       {'user': 'Юля', 'item': 'Айфон'}, 
       {'user': 'Иван', 'item': 'Ноутбук'},
       {'user': 'Сергей', 'item': 'Браслет'},
       {'user': 'Инна', 'item': 'Айфон'},
       {'user': 'Ольга', 'item': 'Айфон'},
       {'user': 'Дмитрий', 'item': 'Браслет'}]

sales_dict = defaultdict(int)

# Добавляем элемент в словарь sales_dict
    # element['item'] - название товара
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1
for element in sales_log:
    sales_dict[element['item']] += 1

# Создаем объект Counter из полученного словаря и используем метод most_common
sales_coun = Counter(sales_dict)
print(f'Самый популярный товар {sales_coun.most_common(1)[0][0]} с числом продаж {sales_coun.most_common(1)[0][1]}')