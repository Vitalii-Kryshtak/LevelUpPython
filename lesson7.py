from random import random
from copy import copy, deepcopy

#Метод sort()
AlphaList = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
NumericList  = [int(random() * 100) for i in range(0, 20)]

#Сортировка по возврастанию
AlphaList.sort()
NumericList.sort()
print('-----Сортировка по возврастанию-----\n', AlphaList, '\n', NumericList)

#Сортировка по убыванию
AlphaList.sort(reverse=True)
NumericList.sort(reverse=True)
print('------Сортировка по убыванию------\n', AlphaList, '\n', NumericList)

#Копирование списков
mainList = ['Boat', 'Fish', '67', 'Fishing Rod', {'AA', 'GG', 'VV'}, {'Name':'Oleg', 'Age':22, 'Gender':'Male'}]
firstList = mainList.copy()
secondList = copy(mainList)
thirdList = deepcopy(mainList)
print('-----Копирование списков list.copy(), copy.copy(), copy.deepcopy()-----')
print("list.copy(), ID [5]: ", id(firstList[5]))
print("copy.copy(), ID [5]: ", id(secondList[5]))
print("copy.deepcopy(), ID [5]: ", id(thirdList[5]))

#Создать список который содержит только цифры
str = "sdhfueiyr37456328579efhigrh4uty44ty73hfwekjfherouty298r23fh’aQWFHWE"

List = [i for i in str if i.isdigit()]
print('-----Список который содержит только цифры-----\n', List)

#Создать список элементы которого делятся на 11
nList = [121, 544, 111, 99, 77]

Update_nList = [i for i in nList if i % 11 == 0]
print('-----Элементы делятся на 11-----\n', Update_nList)

#Создать список с учетом удешевления стоимости на 10%
priceList = [121, 544, 111, 99, 77]

salePriceList = [round(i * 0.9) for i in priceList]
print('-----Список с учетом удешевления стоимости на 10%-----\n', salePriceList)

#Создать список если слово начинается с букви “р”, добавить до слова “my ”
fruit = ['apple', 'pear', 'banana', 'melon', 'pineapple']

my_fruit = ['my ' + i for i in fruit if i[0] == 'p']
print('-----Список начинается с буквы “р” + “my ”-----\n', my_fruit)