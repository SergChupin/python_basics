# 1
print('Задание 1\n')
date_numbers = []


class Date:

    def __init__(self, user_date):
        self.user_date = user_date

    @classmethod
    def extract_date(cls, user_date):
        for i in user_date.split('-'):
            date_numbers.append(int(i))
        return int(date_numbers[0]), int(date_numbers[1]), int(date_numbers[2])

    @staticmethod
    def validation(day, month, year):
        date_numbers[0] = day
        date_numbers[1] = month
        date_numbers[2] = year

        if year > 0:
            if 1 <= month <= 12:
                if month == 2:
                    if year % 4 == 0:  # на случай високосного года.
                        if 1 <= day <= 29:
                            return f"Дата правильная. Високосный год."
                        else:
                            return f"Неверная дата - нет такого числа в этом месяце."
                    if 1 <= day <= 28:
                        return f"Дата правильная."
                    else:
                        return f"Неверная дата - нет такого числа в этом месяце."
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    if 1 <= day <= 31:
                        return f"Дата правильная."
                    else:
                        return f"Неверная дата - нет такого числа в этом месяце."
                else:
                    if 1 <= day <= 30:
                        return f"Дата правильная."
                    else:
                        return f"Неверная дата - нет такого числа в этом месяце."
            else:
                return f"Неверная дата - нет такого месяца."
        return f"Неверное значение года."

    def __str__(self):
        return f"Введена дата: {Date.extract_date(self.user_date)}"


date = Date(input('Введите дату в формате "день-месяц-год":\n'))
print(date)
print(date.validation(date_numbers[0], date_numbers[1], date_numbers[2]))
print('')

# 2
print('Задание 2\n')


class OwnZeroDivision(Exception):

    def __init__(self, txt):
        self.txt = txt


numerator = input('Введите числитель: ')
denominator = input('Введите знаменатель: ')

try:
    numerator = int(numerator)
    denominator = int(denominator)
    if denominator == 0:
        raise OwnZeroDivision("Деление на ноль недопустимо!")
except ValueError:
    print("Вы ввели не число.")
except OwnZeroDivision as err:
    print(err)
else:
    print(f"{numerator} / {denominator} = {numerator / denominator}")


print('')

# задание 3
print('Задание 3\n')
print("Система запрашивает данные (числа), пока пользователь не введёт команду 'stop'.\n")
content_list = []


class OwnContent(Exception):

    def __init__(self, content):
        self.content = content


a = input("Введите число: ")
while a != "stop":
    try:
        a = int(a)
        content_list.append(int(a))
        if a != int(a):
            raise OwnContent("Вы ввели не число.")
        a = input("Введите число: ")
    except ValueError:
        print("Надо вводить только целые числа.")
        a = input("Введите число: ")
else:
    print(f"Итоговый список: {content_list}")

print('')

# 4
print('Задания 4-6\n')
equip_list = []


class Warehouse:

    def __init__(self, square, capacity, workers):
        self.square = square
        self.capacity = capacity
        self.workers = workers


class OfficeEquipment:

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.item = {'Наименование: ': self.name, "Кол-во товаров: ": self.quantity, 'Цена за единицу: ': self.price}

    def get_equipment(self):
        try:
            name = input('Наименование товара: ')
            quantity = int(input('Кол-во товаров: '))
            price = int(input('Цена за единицу: '))
            item = {'Наименование:': name, "Кол-во товаров:": quantity, 'Цена за единицу:': price}
            self.item.update(item)
        except ValueError:
            print('Неверный тип данных!')

    def __str__(self):
        return f"Наименование: {self.name}, Кол-во товаров: {self.quantity}, Цена за единицу: {self.price}."


class Printer(OfficeEquipment):

    def __init__(self, printer_type, name, quantity, price):
        super().__init__(name, quantity, price)
        self.printer_type = printer_type


class Scanner(OfficeEquipment):

    def __init__(self, scan_speed, name, quantity, price):
        super().__init__(name, quantity, price)
        self.scan_speed = scan_speed


class Xerox(OfficeEquipment):

    def __init__(self, pages_per_minute, name, quantity, price):
        super().__init__(name, quantity, price)
        self.pages_per_minute = pages_per_minute


p = Printer('laser', 'Lexmark', 3, 4700)
s = Scanner(3, 'Canon', 5, 6500)
x = Xerox(10, 'Xerox', 7, 8100)
print(f"{p}\n{s}\n{x}\n")
print(p.get_equipment())
print(s.get_equipment())
print(x.get_equipment())
print(f"{p.item}\n{s.item}\n{x.item}\n")


# 7
print('Задание 7\n')


class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b} * j'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} + {self.b * other.a + self.a * other.b} * j'

    def __str__(self):
        return f'{self.a} + {self.b} * j'


comp_number_1 = ComplexNumber(-1, 3)
comp_number_2 = ComplexNumber(4, 2)
print(f"Комплексное число №1 = {comp_number_1}\n"
      f"Комплексное число №2 = {comp_number_2}\n")
print(f"Сумма этих чисел равна: {comp_number_1 + comp_number_2}")
print(f"Произведение этих чисел равно: {comp_number_1 * comp_number_2}")
