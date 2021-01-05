# 1
from abc import ABC, abstractmethod  # к заданию 2
print('Задание 1\n')


class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for j in range(len(other.matrix_list[i])):
                self.matrix_list[i][j] = self.matrix_list[i][j] + other.matrix_list[i][j]
        return Matrix.__str__(self)

    def __str__(self):
        return '\n'.join(map(str, self.matrix_list))


m_1 = Matrix([[1, 2, 3, -1], [4, 5, 6, 2], [7, 8, 9, -3]])
m_2 = Matrix([[9, 8, 7, 1], [6, 5, 4, -2], [3, 2, 1, 3]])
print(f"Matrix #1\n{m_1}\n")
print(f"Matrix #2\n{m_2}\n")
print(f"New Matrix\n{m_1 + m_2}\n")

# 2
print('Задание 2\n')


class Clothes(ABC):

    def __init__(self, param_1):
        self.param_1 = param_1

    @property
    def fabric(self):
        return f"{coat.fabric() + suit.fabric():.2f}"

    @abstractmethod
    def my_method(self):
        pass


class Coat(Clothes):

    def fabric(self):
        return f"{self.param_1 / 6.5 + 0.5:.2f}"

    def my_method(self):
        return "абстрактный класс для пальто"


class Suit(Clothes):

    def fabric(self):
        return f"{(2 * self.param_1 + 0.3) / 100:.2f}"  # делю на 100, чтобы перевести см в метры

    def my_method(self):
        pass


coat = Coat(48)
suit = Suit(175)
print(f"На пошив пальто {coat.param_1} размера нужно {coat.fabric()} метров ткани.")
print(f"На пошив костюма на рост {suit.param_1} см нужно {suit.fabric()} м ткани.")
print(f"Суммарный расход: {float(coat.fabric()) + float(suit.fabric()):.2f} м ткани.")
print(coat.my_method())
print(suit.my_method())
print('')

# 3
print('Задание 3\n')


class Cell:

    def __init__(self, cells_quantity):
        self.cells_quantity = cells_quantity

    def __add__(self, other):
        return f"Объединение двух клеток. Число ячеек общей клетки - {self.cells_quantity + other.cells_quantity}"

    def __sub__(self, other):
        sub_res = self.cells_quantity - other.cells_quantity
        if sub_res > 0:
            return f"Вычитание двух клеток. Результат - {self.cells_quantity - other.cells_quantity}"
        else:
            return f"Вычитание невозможно! Результат меньше либо равен нулю."

    def __mul__(self, other):
        return f"Умножение двух клеток. Число ячеек общей клетки - {self.cells_quantity * other.cells_quantity}"

    def __truediv__(self, other):
        return f"Деление двух клеток. Число ячеек общей клетки - " \
               f"{round(self.cells_quantity / other.cells_quantity)}"

    def make_order(self, cells_in_row):
        cells = ''
        for i in range(int(self.cells_quantity / cells_in_row)):
            cells += '*' * cells_in_row + '\n'
        cells += '*' * (self.cells_quantity % cells_in_row) + '\n'
        return cells


cell_1 = Cell(16)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(3))
