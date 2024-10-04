class Calculator:
    def add(self, a, b):
        return a + b


class StringCalculator(Calculator):
    def add(self, a, b):
        return str(a) + str(b)


calc = Calculator()
print(calc.add(10, 20))

str_calc = StringCalculator()
print(str_calc.add("Hello, ", "World!"))
