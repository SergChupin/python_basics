# 1
import time
print('Задание 1\n')


class Trafficlight:
    __color = None

    def running(self):
        self.__color = "Красный. Ждите."
        print(f"{self.__color}")
        time.sleep(7)
        self.__color = "Жёлтый. Приготовтесь."
        print(f"{self.__color}")
        time.sleep(2)
        self.__color = "Зелёный. Езжайте!"
        print(f"{self.__color}")
        time.sleep(8)


traffic_light = Trafficlight()
traffic_light.running()

print('')

# 2
print('Задание 2\n')


class Road:
    __length = None
    __width = None

    def __init__(self, length, width):
        self.__length = length
        self.__width = width
        self.mass = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self.__length * self.__width * self.mass * self.height / 1000
        print(f"Масса асфальта, необходимая для покрытия дорожного полотона - {round(asphalt_mass)} т")


road = Road(length=5000, width=20)
road.asphalt_mass()
print('')

# 3
print('Задание 3\n')


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker_1 = Position(name='Vasya', surname='Petrov', position='intern', wage='12000', bonus='5000')
worker_2 = Position(name='Masha', surname='Rasteryasha', position='intern', wage='14000', bonus='5500')
print(f"Работник {worker_1.get_full_name()} получит итого {worker_1.get_total_income()} рублей")
print(f"Работник {worker_2.get_full_name()} получит итого {worker_2.get_total_income()} рублей")
print('')

# 4
print('Задание 4\n')


class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехал."

    def stop(self):
        return f"{self.name} остановился."

    def turn(self, direction):
        return f"{self.name} повернул {direction}."

    def show_speed(self):
        return f"Текущая скорость - {self.speed}."


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"Вы превышаете скорость! Ваша скорость {self.speed}."
        else:
            return f"Текущая скорость - {self.speed}."


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"Вы превышаете скорость! Ваша скорость {self.speed}"
        else:
            return f"Текущая скорость - {self.speed}."


class PoliceCar(Car):
    pass


town_car = TownCar(speed=65, color="white", name="Ford", is_police=False)
sport_car = SportCar(120, "Red", "Dodge", False)
work_car = WorkCar(38, "Black", "Chevrolet", False)
police_car = PoliceCar(75, "Blue", "BMW", True)

print(town_car.color, town_car.name, "- это городской автомобиль.", town_car.go(), town_car.show_speed(),
      town_car.turn('налево'), town_car.turn('направо'), town_car.stop())
print(sport_car.color, sport_car.name, "- это спортивный автомобиль.", sport_car.go(), sport_car.show_speed(),
      sport_car.turn('направо'), sport_car.turn('налево'), sport_car.turn('направо'), sport_car.stop())
print(work_car.color, work_car.name, "- это рабочий автомобиль.", work_car.go(), work_car.show_speed(),
      work_car.turn('направо'), work_car.turn('налево'), work_car.stop())
print(police_car.color, police_car.name, "- это полицейский автомобиль.", police_car.go(), police_car.show_speed(),
      police_car.turn('налево'), police_car.turn('направо'), police_car.turn('направо'), police_car.turn('налево'),
      police_car.stop())

print('')

# 5
print('Задание 5\n')


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return f"Будем рисовать {self.title}, чтобы нельзя было стереть."


class Pencil(Stationery):

    def draw(self):
        return f"Для тренировки порисуем {self.title}."


class Handle(Stationery):

    def draw(self):
        return f"Чтобы надолго оставить свой след, будем рисовать {self.title}."


pen = Pen("ручкой")
pencil = Pencil("карандашом")
handle = Handle("маркером")

print(pen.draw())
print(pencil.draw())
print(handle.draw())
