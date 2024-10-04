import random


if __name__ == '__main__':
    # 7 задача практика
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(numbers)
    print()

    my_dict = {
        1: 'apple',
        2: 'banana',
        3: 'orange',
        4: 'cat',
        5: 'dog',
        6: 'mouse',
        7: 'house',
        8: 'tree',
        9: 'flower',
        10: 'book'
    }

    for key, value in my_dict.items():
        print(f'{key}: {value}')
    print()

    # 8 задача практики
    numbers_div_3 = [i for i in range(1, 101) if i % 3 == 0]
    print(numbers_div_3)
    print()

    # 9 задача практики
    for i in range(10):
        print(f'2 * {i} = {2 * i}')
    print()

    # 10 задача практики

    total_count = 0

    for i in range(2, 51):
        for j in range(1, i + 1):
            if i % j == 0:
                total_count += 1

        if total_count <= 2:
            print(i, end=', ')
        total_count = 0
    print('\n')

    # 11 задача практики

    sum_of_squares = 0
    for i in range(1, 11):
        sum_of_squares += i ** 2
    print(sum_of_squares)
    print()

    # 12 задача практики

    for x in range(1, 21, 5):
        y = x ** 2
        print(f"{x}: {y}")