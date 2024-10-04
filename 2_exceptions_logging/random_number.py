import logging
import random


logging.basicConfig(filename='random_number_generator.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def generate_random_number(low, high):
    return random.randint(low, high)


def main():
    try:
        low = int(input("Введите начало диапазона: "))
        high = int(input("Введите конец диапазона: "))

        if low < 0 or high < 0:
            raise ValueError("Границы диапазона не могут быть отрицательными.")
        if low > high:
            raise ValueError("Нижняя граница должна быть меньше или равна верхней границе.")

        random_number = generate_random_number(low, high)
        print(f"Случайное число в диапазоне [{low}, {high}]: {random_number}")
        logging.info(f"Сгенерировано случайное число {random_number} в диапазоне [{low}, {high}].")

    except ValueError as e:
        print(f"Ошибка: {e}")
        logging.error(f"Ошибка ввода границ диапазона: {e}. Попробуйте снова.")


if __name__ == "__main__":
    main()
