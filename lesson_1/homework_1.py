# задание №2
time = int(input("Введите количество секунд: "))

time_hours = time // 3600
time_minutes = time % 3600 // 60
time_seconds = time % 60
time_result = f"{time_hours}:{time_minutes}:{time_seconds}"

print(time_result)

# задание №3
number1 = (input("Введите целое положительное число: "))

number2 = number1 + number1
number3 = number1 + number1 + number1
summ = int(number1) + int(number2) + int(number3)
numbers_summ = f"{number1} + {number2} + {number3} = {summ}"

print(numbers_summ)

# задание №4
number_row = int(input("Введите целое положительное число: "))

max_digit = number_row % 10
number_row = number_row // 10
while number_row > 0:
    if number_row % 10 > max_digit:
        max_digit = number_row % 10
    number_row = number_row // 10
print("Самая большая цифра в этом числе -", max_digit)

# задание №5
income = int(input("Введите значение выручки: "))
costs = int(input("Введите значение издержек: "))
profit = income - costs
loss = costs - income
pure_income = profit / income
if income > costs:
    print("Прибыль:", profit)
    print("Рентабельность:", pure_income * 100, "%")
else:
    print("Убыток:", loss)

personel = int(input("Введите численность сотрудников: "))
profit_per_capita = profit / personel
print("Прибыль на одного сотрудника: ", profit_per_capita)

# Задание №6
a = int(input("Введите результат первого дня, в км: "))
b = int(input("Введите желаемый результат, в км: "))
day = 1
while a < b:
    day = day + 1
    a = a * 1.1
answer = f"На {day} день спортсмен достиг результата - не менее {b} км"
print(answer)
