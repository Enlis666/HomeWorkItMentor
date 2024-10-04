import numpy as np


def calculate_square_values(start, end, step):
    x_elem = np.arange(start, end + step, step)
    y_elem = x ** 2
    return x_elem, y_elem


if __name__ == '__main__':
    x_values, y_values = calculate_square_values(1, 10, 0.5)

    for x, y in zip(x_values, y_values):
        print(f"x = {x:.1f}, y = {y:.2f}")
