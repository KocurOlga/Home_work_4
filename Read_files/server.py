file_object = open('D:\\Python\\PumpSkill\\module4\\Read_files\\input.txt', 'r', encoding='utf-8')
file_content = file_object.read()
list_of_number = file_content.split(',')
file_output = open('D:\\Python\\PumpSkill\\module4\\Read_files\\output.txt', 'w', encoding='utf-8')
for num in list_of_number:
    if int(num) % 2 == 0:
        file_output.write(num + ',')
file_output.close
