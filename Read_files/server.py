# Импортируем библиотеку pandas
import pandas


# Читаем файл эксель и результат передаем в переменную excel_data
# Переменная excel_data имеет тип <class 'pandas.core.frame.DataFrame'>
excel_data = pandas.read_excel('data.xlsx', sheet_name='users')

# Преобразуем переменную excel_data в словарь с помощью метода to_dict()
# Результат передаем в переменную excel_data_dict
excel_data_dict = excel_data.to_dict(orient='records')

print(excel_data_dict)
print(type(excel_data_dict))
