#воспользуемся знакомой функцией
def get_value_from_list(object_list, separator, key):
    """Функция находит значение ключа key из списка object_list
    по разделителю separator
    :param object_list: список строк
    :param separator: разделитель
    :param key: искомый ключ"""
    
    value = None
    for element in object_list:
        words = element.split(separator)
        if words[0] == key:
            value = words[1]
            break
    return value

#список для результата
cheaper_list = []

log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

string = log.split('\n')

for records in string:#проходим по каждой из строк log
    record_list = records.split(';')
    #"вытаскиваем" нужные нам параметры
    #стоимость для проверки на условие (<13000)
    #наименование для занесения в список
    cheaper_cost = get_value_from_list(record_list, ':', 'item_cost')
    cheaper_item = get_value_from_list(record_list, ':', 'item')
    if int(cheaper_cost) < 13000:
        if cheaper_item not in cheaper_list: #проверка на наличие такого наименования в списке
            cheaper_list.append(cheaper_item)

print(*cheaper_list, sep=', ')
