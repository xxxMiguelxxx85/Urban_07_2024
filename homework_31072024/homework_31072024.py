# --------Работа со словарем--------
my_dict = {'Sergey' : 1985, 'Polina' : 1985, 'Milana' : 2015} # - Создайте переменную и присваиваеи ей словарь из нескольких пар ключ-значение
print(my_dict)
print(my_dict['Sergey']) # - Выведите на экран одно значение по существующему ключу
my_dict['Milana'] = 2015
print(my_dict) # - одно по отсутствующему из словаря
# или же ====>
print(my_dict.get('Max', 'Такого ключа, в Вашем словаре нет'))
my_dict.update({'Katrin' : 1987,
                'Roman' : 1982}) # - Добавьте ещё две произвольные пары того же формата в словарь
print(my_dict)
print(my_dict.pop('Katrin')) # - Удалите одну из пар в словаре по существующему ключу из словаря
print(my_dict)
# --------РАбота с множество--------
my_set = [1, 3, 'Urban', 3, 5, 2, 4, 'Sergey', True, (5, 7, 6), 'Sergey'] # - Создайте переменную и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = set(my_set)
print(my_set.add(1985)) # - Добавьте произвольных элемента в множество, которых ещё нет
print(my_set.add('Milana')) # - Добавьте произвольных элемента в множество, которых ещё нет
print(my_set)
print(my_set.remove('Urban')) # - Удалите один любой элемент из множества
print(my_set)
