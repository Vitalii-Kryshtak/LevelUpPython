from random import random
#Home work 8

#Используя инструкцию while разработать программу, которая вычисляет сумму элементов списка.
integer_list = [int(random() * 100) for i in range(0, 10)]  # Create random list
sum = 0
i = 0
while i < len(integer_list):
    sum += integer_list[i]
    i += 1

print("Сумма элементов списка равна: ", sum)
print("-" * 50)

#Из чисел 1+1/2, 1+1/3, 1+1/4 …, напечатать те, которые не меньше a.
while True:
    a = float(input("Введите число a (1 < a < 1.5): "))
    if 1 < a < 1.5:
        divisor = 2
        compared_number = 1 + 1 / divisor
        while a < compared_number:
            print(compared_number)
            divisor += 1
            compared_number = 1 + 1 / divisor
        break

print("-" * 50)

#В каждой строке подсчитать количество вхождений заданного любого символа
book = ['Lorem Ipsum is simply dummy text', 'Latin professor College in Virginia', 'from a Lorem Ipsum passage', 'standard chunk']
user_value = input("Введите искомый символ: ")
count_user_value = []
for part_book in book:
    if part_book.find(user_value):
        number_string  = book.index(part_book)
        count_value = part_book.count(user_value)
        count_user_value.append(f"В строке № {number_string} - {count_value} вхождения")

print(count_user_value)
print("-" * 50)

#4.	Пользователь вводит число. Если элемент не найден, то выводится соответствующее сообщение.
default_list = [2, 8, 3, 4, 3, 5, 2, 1, 0, 3, 4, 4, 5, 8, 7, 7, 5]
user_number = input("Введите число от 0 до 9: ")


'''Используя цикл FOR'''

for number in default_list:
    if int(user_number) == number:
        print(f"Число {user_number} есть в списке")
        break
else:
    print(f"Число {user_number} отсутствует в списке")

'''Иначе это можно сделать так:'''

if int(user_number) in default_list: print(f"Число {user_number} есть в списке")
else: print(f"Число {user_number} отсутствует в списке")
