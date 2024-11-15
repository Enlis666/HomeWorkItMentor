# 1. Используя операции индексирования и среза выведите на экран первый и третий элементы списка [1, 2, 3 ,4 ,5],
#    а также срез списка из первых трех элементов
array = [1, 2, 3, 4, 5]
print(f'Первый и третий элемент из списка [1, 2, 3 ,4 ,5] = {array[0]} и {array[2]}')
print(f'Cрез из первых трех элементов: {array[:3]}')

# 2. Дан список [«Ростов», «+», «на», «-», «Дону»].
#    Исправьте плюс на дефис и выведите название города на экран использовав доступ к элементам списка по индексам
array = ['Ростов', '+', 'на', '-', 'Дону']
index = array.index('-')
array[index] = '+'
print(f'{array}')

# 3. Дан список [«a», «s», «1», «a», «32», «23»]. Разбейте его на два списка: только с буквами и только с числами. 
array = ['a', 's', 1, 'a', 32, 23]
list_letter = [i for i in array if isinstance(i, str)]
num_letter = [i for i in array if isinstance(i, int)]
print(list_letter, num_letter)

# 4. В предыдущей задаче должен был получиться список из букв.
#    Используя методы списков: удалите из него последний элемент, сделайте реверсию списка.
list_letter.pop()
print(list_letter, list_letter[::-1])

# 5. Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран. Что изменилось?
array = ['a', 's', 1, 'a', 32, 23]
print(set(array))