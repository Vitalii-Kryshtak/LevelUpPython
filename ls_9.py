#Создать из них список кортежей  - list_c = [(1,5), (2,6), (3,7), (4,8)]
list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]
list_c = [tuple_element for tuple_element in zip(list_a, list_b)]
print(list_c)

# Дано список / Создать кортеж ("foo", "bar", "baz", "qux", "etc")
default_list = ["bar", "baz", "qux", "etc"]
default_list.insert(0, 'foo')
my_tuple = tuple(default_list)
print(my_tuple)

# Задано список my_list = (1, 2, 3, 4, 5)
# Получите шестой єлемент списка. В случае его отсутствия отсутствия видайте відайте сообщение о его отсутствии
my_list = [1, 2, 3, 4, 5]
try:
    print(my_list[6])
except IndexError:
    print('Элемента с таким индексом в списке нет')