immutable_var = tuple([1, 2, 3, True, "String"]) # - Создаем переменную и присваиваем ей кортеж из нескольких элементов разных типов данных
print(immutable_var)
#immutable_var[3] = False # - так как в первом задании практического задания, мы создать кортеж (tuple)!
# При выводе обращения к внутренним элементам кортежа, мы получим ошибку. Это связано с тем, что внтрение элементы кортежа не изменяемые!!!
#print(immutable_var)
mutable_list_ = ([3, 4, 5, False, "String"]) # - Создаем переменную и присваиваем ей список из нескольких элементов разных типов данных
print(mutable_list_)
mutable_list_[0] = 9 # - Так как кортеж не изменяемый, будем изменять элементы внутри списка
mutable_list_[1] = 1
mutable_list_[2] = 1
mutable_list_.append('Urban')
print(mutable_list_)
mutable_list_.remove("String")
print(mutable_list_)
mutable_list_[3] = True
print(mutable_list_)
print(1 in mutable_list_)
print(7 in mutable_list_)