# 1
print('Задание 1')
print('')

from sys import argv

salary = argv
working_hours = int(input("Укажите выработку в часах: "))
hour_pay = int(input("Введите ставку за 1 час: "))
bonus = int(input("Введите размер премии: "))
salary = (working_hours * hour_pay) + bonus
print(f"Итоговая зарплата сотрудника составляет: {salary}")
print('')

# 2
print('Задание 2')
print('')

list_2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([list_2[el] for el in range(1, len(list_2)) if list_2[el] > list_2[el - 1]])
print('')

# 3
print('Задание 3')
print('')

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])
print('')

# 4
print('Задание 4')
print('')

list_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([el for el in list_4 if list_4.count(el) == 1])
print('')

# 5
print('Задание 5')
print('')

from functools import reduce

list_5 = [el for el in range(100, 1001) if el % 2 == 0]
def my_func_5(prev_el, el):
    return prev_el * el

print(reduce(my_func_5, list_5))
print('')

# 6
print('Задание 6')
print('')

from itertools import count, cycle

# а)
a = (int(input("Введите целое число: ")))
for el in count(a):
    if el >= a + 5:
        break
    print(el)

print('')

# б)
list_6 = ['Example', 53124, None, True]
print(f"Список элементов для поочерёдного вывода в повторяющемся цикле: {list_6}")
b = int(input("Введите количество циклов вывода элементов: "))

c=0
for el in cycle(list_6):
    if c == b:
        break
    print(el)
    c += 1

print('')

# 7
print('Задание 7')
print('')

from math import factorial

n = int(input("Введите число: "))
def fact(n):
    for item in count(1):
        if n >= item:
            yield factorial(item)

for el in fact(n):
    print(el)
