first = int(input('Введите первое целое число: '))
second = int(input('Введите второе целое число: '))
third = int(input('Введите третье целое число: '))

if first == second and second == third and third == first: # - Если все числа равны между собой, то вывести 3
    print(3)
elif first == second or second == third or third == first: # - Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    print(2)
else:
    print(0) # - Если равных чисел среди 3-х вообще нет, то вывести 0
