def binary_search(arr,  tg):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == tg:
            return mid
        elif arr[mid] < tg:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 7

    result = binary_search(array, target)

    if result != -1:
        print(f"Элемент найден на индексе {result}")
    else:
        print("Элемент не найден")
