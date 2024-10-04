import logging


logging.basicConfig(filename='errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_average(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Входные данные должны быть списком.")

        for num in numbers:
            if not isinstance(num, (int, float)):
                raise ValueError(f"Все элементы должны быть числами. Некорректный элемент: {num}")

        return sum(numbers) / len(numbers)

    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
        return f"Произошла ошибка: {e}"


if __name__ == "__main__":
    test_data = [1, 2, 3, 4, 5]
    result = calculate_average(test_data)
    print(result)
