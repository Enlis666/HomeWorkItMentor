class Dog:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} гав!"

    def fetch(self, item):
        return f"{self.name} несу {item}"


dog1 = Dog("Джессика", "Лабрадор", 5)
dog2 = Dog("Макс", "Бульдог", 3)

print(dog1.bark())
print(dog2.fetch("мяч"))

print(dog1 is dog2)
