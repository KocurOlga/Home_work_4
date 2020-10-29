#константы, которые передаются в список user_list
GENDER_MALE = 'm'
GENDER_FEMALE = 'f'

user_list = [{'name': 'Ivan', 'gender': GENDER_MALE},
             {'name': 'Olga', 'gender': GENDER_FEMALE},
             {'name': 'Anna', 'gender': GENDER_FEMALE},
             {'name': 'Petr', 'gender': GENDER_MALE}]

male_count = 0
female_count = 0

for user in user_list:
    if user['gender'] == GENDER_MALE:
        male_count += 1
    else:
        female_count += 1

print('Мужчин в списке', male_count)
print('Женщин в списке', female_count)
