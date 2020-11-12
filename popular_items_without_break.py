#константы, которые передаются в список user_list
GENDER_MALE = 'm'
GENDER_FEMALE = 'f'

#список пользователей
user_list = [{'name': 'Иван', 'gender': GENDER_MALE},
             {'name': 'Петр', 'gender': GENDER_MALE},
             {'name': 'Марья', 'gender': GENDER_FEMALE},
             {'name': 'Дарья', 'gender': GENDER_FEMALE},
             {'name': 'Юлия', 'gender': GENDER_FEMALE}]

#список товаров
item_list = [{'title': 'Часы', 'cost': 9800},
             {'title': 'Кофемашина', 'cost': 23500},
             {'title': 'Фитнес-браслет', 'cost': 13200},
             {'title': 'Айфон', 'cost': 73900},
             {'title': 'Чехол для телефона', 'cost': 250}]

#журнал регистрации какой пользователь что купил
log = [{'user': user_list[0], 'purchases': [item_list[0], item_list[1], item_list[2]]},
       {'user': user_list[1], 'purchases': [item_list[0], item_list[2]]},
       {'user': user_list[2], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[3], 'purchases': [item_list[2], item_list[3]]},
       {'user': user_list[4], 'purchases': [item_list[4], item_list[2]]}]

# Создадим список для хранения популярных товар: popular_items.
popular_items = []

# Обходим все записи из списка log
for record in log:
    # Для каждой записи из списка 'log' в цикле обходим все записи из списка 'purchases'
    for item in record['purchases']:
        # Получаем название купленного товара
        purchase_title = item['title']
        # Ищем купленный товар в списке popular_items по ключу 'title'
        found = False
        i = 0 #счетчик для контроля конца цикла
        for popular_item in popular_items:
            #проверяем одновременно найден ли элемент и не достигли ли конца списка
            if not found and i < len(popular_items): 
                if popular_item['title'] == purchase_title:
                    popular_item['quantity'] += 1
                    found = True
                    i = len(popular_items)#замена break - типа дошли до конца списка
        # Если купленный товар не найден в списке popular_items,
        # то добавляем его и ставим количество (quantity) = 1
        if not found:
            popular_items.append({'title': purchase_title, 'quantity': 1})
        print(popular_items)
# Выводим продажи по каждому товару
for popular_item in popular_items:
    print(f"Количество продаж товара {popular_item['title']} = {popular_item['quantity']}")

#определяем максимальной количество продаж
max_count = 0
popular_item_title = ''
for quant in popular_items:
    if max_count < quant['quantity']:
        max_count = quant['quantity']
        popular_item_title = quant['title']
print(f'Самый популярный товар {popular_item_title} с числом продаж {max_count}')
