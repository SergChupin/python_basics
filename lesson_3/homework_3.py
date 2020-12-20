# задание 1
print('Задание 1')

def div_func():
    """
    Вы вводите последовательно два числа.
    Получаете результат деления первого числа на второе.
    """
    print(div_func.__doc__)
    arg_1 = int(input('Введите первое число: '))
    arg_2 = int(input('Введите второе число: '))
    if arg_2 == 0:
        return "На ноль делить нельзя!"
    return arg_1 / arg_2

div_res = div_func()
print(div_res)

print('')

# задание 2
print('Задание 2')
print('')

def user_data(first_name, last_name, birth_year, city, email, phone):
    print(
        f"Имя - {first_name}, "
        f"фамилия - {last_name}, "
        f"год рождения - {birth_year}, "
        f"город проживания - {city}, "
        f"e-mail - {email}, "
        f"телефон - {phone}.") # записал так, а не в одну строку для удобства восприятия.

first_name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
birth_year = input('год рождения: ')
city = input('город проживания: ')
email = input('e-mail: ')
phone = input('номер телефона: ')
user_data(
    first_name=first_name,
    last_name=last_name,
    birth_year=birth_year,
    city=city,
    email=email,
    phone=phone) # здесь тоже не в строку, т.к. получалось слишком длинно.

print('')

# задание 3
print('Задание 3')

def my_func(arg_31, arg_32, arg_33):
    """
    Вы вводите 3 числа, получаете сумму двух наибольших.
    """
    print(my_func.__doc__)
    arg_31 = int(input("Введите первое число: "))
    arg_32 = int(input("Введите второе число: "))
    arg_33 = int(input("Введите третье число: "))
    if arg_31 >= arg_33 and arg_32 >= arg_33:
        return arg_31 + arg_32
    elif arg_31 > arg_32 and arg_32 < arg_33:
        return arg_31 + arg_33
    else:
        return arg_32 + arg_33

print(f"Сумма двух наибольших чисел равна {my_func(int, int, int)}")
print('')

# задание 4
print('Задание 4')

def my_func_4(x, y):
    """
    Возведение числа X в отрицательную степень Y.
    """
    print(my_func_4.__doc__)
    x = int(input('Введите число: '))
    y = int(input('Введите отрицательную степень: '))
    if y == 0:
        return 1
    return x ** y


print(my_func_4(int, int))

print('')

# задание 5
print('Задание 5')
print('')

numbers_sum = 0
exit = False

while True:
    numbers = input('Введите числа через пробел: ').split()
    for item in numbers:
        if item == "q":
            exit = True
            break
        if not item.isdigit():
            print(f"{item} не является числом")
            break
        numbers_sum += int(item)
    print(f"Сумма равна {numbers_sum}. Для завершения введите q")
    if exit:
        print(f"Сумма равна {numbers_sum}.")
        break

print('')

# задание 6
print('Задание 6')
print('')

text = input('Введите текст: ')
def int_func():
    return text.capitalize()

print(int_func())

def int_func_2():
    return text.title()

print(int_func_2())
