import time


def total_time(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        result_time = round((time.time() - start) * 1000, 5)
        print(f'Время выполнения функии: {result_time}')
    return wrapper


# @total_time
def bubble_sort(arr: list) -> list:

    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == '__main__':
    array = [81, 50, 4, 27, 34, 5, 90]
    bubble_sort(array)
    print(f'Отсортированный список:  {array}')
