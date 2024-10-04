# 1. Дано расстояние L в сантиметрах.
#    Используя операцию деления нацело, найти количество полных метров в нем (1 метр = 100 см).
L = 163
print(f'Кол-во полных метров в {L}см = {L // 100}м')

# 2. Дана масса M в килограммах.
#    Используя операцию деления нацело, найти количество полных тонн в ней (1 тонна = 1000 кг).
M = 16310
print(f'\nКол-во полных тон в {M}кг = {M // 1000}т')

# 3. Дан размер файла в байтах. Используя операцию деления нацело,
#    найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).
M = 16310
print(f'\nКол-во полных киллобайтов в {M} б = {M // 1024}кб')

# 4. Даны целые положительные числа A и B (A > B).
#    На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
#    Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.
A, B = 126, 6
print(f'\nКол-во отрезков длинной {B} на основной длине {A} = {A // B}')

# 5. Даны целые положительные числа A и B (A > B).
#    На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
#    Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.
A, B = 127, 6
print(f'\nОстаток от деления чисел {A}, {B} нацело = {A % B}')

# 6. Дано двузначное число. Вывести вначале его левую цифру (десятки), а затем — его правую цифру (единицы).
#    Для нахождения десятков использовать операцию деления нацело,
#    для нахождения единиц — операцию взятия остатка от деления.
a = 67
print(f'\nДанно число: {a}. Его левое число: {a // 10}. Его правое число: {a % 10}')

# 7. Дано двузначное число. Найти сумму и произведение его цифр.
a = 67
l, r = a // 10, a % 10
print(f'\nДанно число: {a}. Сумма его чисел: {l + r}. Произведение его чисел: {l * r}')

# 8. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа..
a = 67
l, r = a // 10, a % 10
print(f'\nДанно число: {a}. Сумма при перестановки его чисел: {r + l}.')

# 9. Дано трехзначное число. Используя одну операцию деления нацело, вывести первую цифру данного числа (сотни).
a = 671
print(f'\nДанно число: {a}. Его первая цифра: {a // 100}')

# 10. Дано трехзначное число. Вывести вначале его последнюю цифру (единицы), а затем — его среднюю цифру (десятки).
a = 671
print(f'\nДанно число: {a}. Его последняя цифра: {a % 10}. Его вторая цифра: {a % 100 // 10}')
