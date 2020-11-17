import pandas


def get_password(object_list, login):
    """Функция находит значение ключа password из списка object_list
    :param object_list: список словарей со структурой login-password
    :param login: искомый login"""

    value = None
    for records in object_list:
        if records['login'] == login:
            value = records['password']
            break
    return value
user_list = pandas.read_excel('data.xlsx', sheet_name='users')
user_dict = user_list.to_dict(orient='records')


#запросим login и password
user_name = input('Введите имя пользователя: ')
user_password = input('Введите пароль: ')

sales_list = pandas.read_excel('data.xlsx', sheet_name='sales')

if get_password(user_dict, user_name) == int(user_password):
    print(sales_list)
else:
    print('Вы ввели неверный логин/пароль')
