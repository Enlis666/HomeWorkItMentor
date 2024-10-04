
if __name__ == '__main__':
    numbers_list = list()
    while True:
        number = int(input('ВВедите число: '))

        if number == 0:
            break

        numbers_list.append(number)

    result = sum(numbers_list) // len(numbers_list)

    print(f'Средние значение введных чисел: {result}')