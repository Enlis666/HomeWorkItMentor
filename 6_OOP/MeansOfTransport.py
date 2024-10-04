class MeansOfTransport:
    def __init__(self, color, car_brand):
        self._color = color
        self._car_brand = car_brand

    def show_color(self):
        print(f'Car color: {self.color}')

    def car_brand(self):
        print(f'Car brand: {self.car_brand()}')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._car_brand = value


class Car(MeansOfTransport):
    car_drive = 4

    def __init__(self, color, car_brand, number_wheels):
        super().__init__(color, car_brand)
        self.__number_wheels = number_wheels

    @classmethod
    def get_car_drive(cls):
        return cls.car_drive

    @staticmethod
    def time_calculation(v, s):
        return round(v / s, 2)

    def get_number_wheels(self):
        return self.__number_wheels

    # Представление объекта
    def __str__(self):
        return f'{self.car_brand} {self.color}, {self.__number_wheels} wheels'

    def __repr__(self):
        return f'Car(color={self.color}, car_brand={self.car_brand}, number_wheels={self.__number_wheels})'

    # Арифметические операции
    def __add__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels + other.__number_wheels
        raise TypeError("Addition only supported between Car instances")

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels - other.__number_wheels
        raise TypeError("Subtraction only supported between Car instances")

    # Сравнение
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels == other.__number_wheels
        return False

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels < other.__number_wheels
        return False

    def __le__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels <= other.__number_wheels
        return False

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels > other.__number_wheels
        return False

    def __ge__(self, other):
        if isinstance(other, Car):
            return self.__number_wheels >= other.__number_wheels
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # Хэширование
    def __hash__(self):
        return hash((self.color, self.car_brand, self.__number_wheels))

    # Работа с атрибутами
    def __getattr__(self, name):
        return f"Attribute '{name}' not found"

    def __setattr__(self, name, value):
        if name == '_Car__number_wheels' and value < 0:
            raise ValueError("Number of wheels cannot be negative")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        if name == '_Car__number_wheels':
            raise AttributeError("Cannot delete number_wheels")
        super().__delattr__(name)


class Moped(MeansOfTransport):
    def __init__(self, color, car_brand, number_wheels):
        super().__init__(color, car_brand)
        self.number_wheels = number_wheels



if __name__ == '__main__':
    test = Car('test', 'test_brand', 4)
    test2 = Car('test', 'test_brand', 2)
    print(test + test2)

