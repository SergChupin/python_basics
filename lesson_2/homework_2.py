# задание 1
print('Задание 1')
print('')

hw_list = [None, 'random text', 25, 199.99, 'string', True]
for el in hw_list:
    print(f"Элемент - {el}, тип элемента - {type(el)}")
print('')

# задание 2
print('Задание 2')
print('')

hw_list_2 = list(input('Введите элементы списка: '))
print(f"Ваш список: {hw_list_2}")
for a in range(1, len(hw_list_2), 2):
    hw_list_2[a - 1], hw_list_2[a] = hw_list_2[a], hw_list_2[a - 1]

print(f"Изменённый список: {hw_list_2}")
print('')

# задание 3
print('Задание 3')
print('')

month = int(input("Введите месяц числом от 1 до 12: "))
while month > 12:
    print("Слишком большое число")
    month = int(input("Введите месяц числом от 1 до 12: "))
while month < 1:
    print("Слишком маленькое число")
    month = int(input("Введите месяц числом от 1 до 12: "))

month_list = [
    "зимний",
    "зимний",
    "весенний",
    "весенний",
    "весенний",
    "летний",
    "летний",
    "летний",
    "осенний",
    "осенний",
    "осенний",
    "зимний"]

month_dict = {
    1: 'зимний',
    2: 'зимний',
    3: 'весенний',
    4: 'весенний',
    5: 'весенний',
    6: 'летний',
    7: 'летний',
    8: 'летний',
    9: 'осенний',
    10: 'осенний',
    11: 'осенний',
    12: 'зимний'}

print(f"{month} - это {month_list[month - 1]} месяц")
print(f"{month} - это {month_dict[month]} месяц")
print('')

# задание 4
print('Задание 4')
print('')

user_msg = input("Напишите несколько слов: ")
user_msg_list = user_msg.split()
i = 1
for elem in user_msg_list:
    print(f"{i}: {elem[:10]}")
    i += 1

print('')

# задание 5
print('Задание 5')
print('')

rating_list = [9, 7, 5, 5, 2, 1]
print(f"Старый рейтинг: {rating_list}")

rating_count = 1
while rating_count <= 3:
    user_rating = int(input("Добавьте новый элемент рейтинга: "))
    i = 0
    for element in rating_list:
        if user_rating <= element:
            i += 1
    rating_list.insert(i, user_rating)
    print(f"Новый рейтинг: {rating_list}")
    rating_count += 1
