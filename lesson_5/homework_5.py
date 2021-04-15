# 1
print('Задание 1 \n')

with open("file1.txt", "w", encoding="utf-8") as f_obj:
    list_1 = []
    while True:
        file_1_str = input("Введите данные: \n")
        if file_1_str == '':
            break
        list_1.append(file_1_str)
    f_obj.writelines(list_1)

# 2
print('Задание 2 \n')

line_count = 0
with open("file2.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        words = line.split()
        print(f"В строке '{line}' {len(words)} слов")
        line_count += 1

print(f"Всего строк: {line_count}")
print('')

# 3
print('Задание 3 \n')

with open("file3.txt", "r", encoding="utf-8") as f_obj:
    less_list = []
    salary = []
    for line in f_obj:
        line = line.split()
        if int(line[1]) < 20000:
            less_list.append(line[0])
        salary.append(line[1])
    print(f"Сотрудники с окладом менее 20000: {less_list}")

print(f"Средняя величина дохода сотрудников: {sum(map(int, salary)) / len(salary)} \n")


# 4
print('Задание 4 \n')

dict_4 = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_4_rus = []

with open("file4.txt", "r") as f_obj:
    for i in f_obj:
        i = i.split(' ', 1)
        file_4_rus.append(dict_4[i[0]] + " " + i[1])
    print(file_4_rus)

print('')

with open("file4_rus.txt", "w", encoding="utf-8") as f_obj_2:
    f_obj_2.writelines(file_4_rus)

# 5
print('Задание 5 \n')

def summ():
    try:
        with open("file5.txt", "w+") as f_obj:
            numbers = input("Введите числа через пробел: ")
            f_obj.writelines(numbers)
            numbers_list = numbers.split()

        print(f"Сумма всех введённых чисел равна {sum(map(int, numbers_list))}")
    except IOError:
        print("Произошла ошибка ввода-вывода!")
    except ValueError:
        print("Произошла ошибка ввода-вывода!")
summ()

print('')

# 6
print('Задание 6 \n')

dict_6 = {}
with open("file6.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        subj, lectures, practice, lab = line.split()
        dict_6[subj] = int(lectures) + int(practice) + int(lab)

print(dict_6)
print('')

# 7
print('Задание 7 \n')

import json

profit = {}
avg_profit = {}
profit_sum = 0
avg_sum = 0
i = 0

with open("file7.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        name, firm, income, expences = line.split()
        profit[name] = int(income) - int(expences)
        if profit.setdefault(name) > 0:
            profit_sum += profit.setdefault(name)
            i += 1
        avg_sum = profit_sum / i
    avg_profit = {"Средняя прибыль": round(avg_sum)}
    print(f"Прибыль каждой компании - {profit}")
    print(avg_profit)

with open("file7.json", "w") as write_j:
    json.dump(profit, write_j)

    json_str = json.dumps(profit)
