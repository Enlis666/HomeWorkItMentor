# 1. Создайте словарь содержащий данные о человеке.
#    В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
dict_data_people = {
    'name': 'Andrey',
    'age': 25,
    'gender': 'male',
    'height': 176,
    'weight': 74,
    'foot size': 44,
}

# 2. Выведите на экран все данные о человеке по ключам.
print('Данные о человеке:')

for i in dict_data_people:
    print(i, ':', dict_data_people[i])

# 3. Добавьте в словарь ключ и значение размера ноги
dict_data_people['foot size'] = 43
print(dict_data_people)

# 4. Добавьте в словарь ключ и значение размера ноги
dict_data_people.pop('foot size')
print(dict_data_people)
