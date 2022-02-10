my_dict = {'Value_1': 1, 'Value_2': 2, 'Value_3': 3, 'Value_4': 4, 'Value_5': 5}
print(id(my_dict))  #2262696638144
my_dict['Value_1'], my_dict['Value_5'] = my_dict['Value_5'], my_dict['Value_1']
my_dict.pop('Value_2')
my_dict.update({'new_key': 'new_value'}) #я думаю так более очевидно что элемент добавляется, нежели ниже
my_dict['new_key'] = 'new_value'
print(id(my_dict))  #2262696638144

#Получить значение по ключу "marks"
student = {"name": "Emma", "class": 9, "marks": 75}
value_marks = student['marks'] #или если не уверены что такой ключ существует:
value_marks_1 = student.get('marks')

#Что выведет этот код?
p = {"name": "Mike", "salary": 8000}
print(p.get("age")) # None

#Как получить "d"
sample = {"1":["a","b"], "2":["c","d"]}
value_d = sample['2'][1]
print(value_d)

#Для каждого города укажите, в какой стране он находится
list_1 = ["Украина-Киев", "Россия-Сочи", "Беларусь-Минск", "Япония-Токио", "Германия-Мюнхен"]
list_2 = ["Киев", "Токио", "Минск"]
temp_dict = dict(value.split('-') for value in list_1)
new_dict = dict()
for key, value in temp_dict.items():
    if value in list_2:
        new_dict[key] = value
print(new_dict)

#Сгенерировать словарь-шифратор
from random import randint
keys_list = [chr(key + 32) for key in range(65, 91)]
values_dict = [chr(key + 32) for key in range(90, 64, -1)]
encoder_dict = {key: value for key, value in zip(keys_list, values_dict)}
same_string = 'The standard chunk of Lorem Ipsum used since the is reproduced below for those interested'
secret_string = ''

for character in same_string:
    if character == ' ':
        secret_string += ' '
    else:
        secret_string += encoder_dict[character.lower()]
decoder_string = ''

for character in secret_string:
    if character == ' ':
        decoder_string += ' '
    else:
        decoder_string += list(encoder_dict.keys())[list(encoder_dict.values()).index(character)]

print(same_string)
print(secret_string)
print(decoder_string)

#Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб.
random_dict = {key : key ** 3 for key in range(1, 11)}
print(random_dict)

#Создайте словарь из строки: в качестве ключей возьмите буквы строки, а значениями пусть будут числа,
# соответствующие количеству вхождений данной буквы в строку
random_string = 'Contrary to popular belief, Lorem Ipsum is not simply random text'
random_dict = dict()
for char in random_string:
    if char.isalpha() and random_dict.get(char) == None:
        random_dict[char] = random_string.count(char)
print(random_dict)

#Создайте словарь, связав его с переменной school
#а) в одном из классов изменилось количество учащихся
# б) в школе появился новый класс
# с) в школе был расформирован (удален) другой класс
# Вычислите общее количество учащихся в школе.
school = {'1a': 15, '2b': 21, '3a': 18, '4s': 25, '5g': 17, '6b': 31, '7d': 28}
school['2b'] = 27
school.update({'8a': 20})
school.pop('5g')
pupil_in_school = 0
for _, value in school.items():
    pupil_in_school += value
print(pupil_in_school) #164

#Создайте словарь, где ключами являются числа, а значениями – строки.
#Создайте функционал которий вернет новый словарь, "обратный" исходному
dict_num_alpha = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k'}
dict_alpha_num = {value : key for key, value in dict_num_alpha.items()}#
