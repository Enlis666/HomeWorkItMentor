import logging
import math


logging.basicConfig(filename='quadratic_solver.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def quadratic(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        logging.error("Дискриминант отрицателен. Уравнение не имеет действительных корней.")
        raise ValueError("Дискриминант отрицателен. Попробуйте другие коэффициенты.")

    sqrt_disc = math.sqrt(discriminant)
    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)

    logging.info(f"Найденные корни уравнения: x1 = {x1}, x2 = {x2}")
    return x1, x2


def main():
    a, b, c = 2, 70, 3
    try:
        x1, x2 = quadratic(a, b, c)
        print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")

    except ValueError as e:
        print(f"Ошибка: {e}")
        logging.info(f"Пользователь ввел неверные коэффициенты: {a}, {b}, {c}. Попробуйте снова.")


if __name__ == "__main__":
    main()
