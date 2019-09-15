# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]


def students_count(students):
    count_names = {}
    for elem in students:
        if count_names.get(elem['first_name']) is None:
            count_names[elem['first_name']] = 1
        else:
            count_names[elem['first_name']] += 1
    return count_names


count_names = students_count(students)
for elem in count_names.keys():
    print(f'{elem}: {count_names[elem]}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

count_names = students_count(students)


def find_frequent_name(count_names):
    frequent_name_count = 0
    frequent_name = ''

    for elem in count_names.keys():
        if count_names[elem] > frequent_name_count:
            frequent_name_count = count_names[elem]
            frequent_name = elem
    return frequent_name


frequent_name = find_frequent_name(count_names)
print(f'Самое частое имя среди учеников: {frequent_name}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

for num, one_class in enumerate(school_students):
    count_names = students_count(one_class)
    frequent_name = find_frequent_name(count_names)
    print(f'Самое частое имя в классе {num + 1}: {frequent_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}


def gender_count(one_class):
    boys_count = 0
    girls_count = 0
    for student in one_class['students']:
        if is_male[student['first_name']] is True:
            boys_count += 1
        else:
            girls_count += 1
    return one_class["class"], girls_count, boys_count


for one_class in school:
    class_name, girls_count, boys_count = gender_count(one_class)

    print(f'В классе {one_class["class"]} {girls_count} девочки и {boys_count} мальчика.')

# ???



# Пример вывода:

# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

max_girls_class = ''
max_girls_count = 0
max_boys_class = ''
max_boys_count = 0
for one_class in school:
    class_name, girls_count, boys_count = gender_count(one_class)
    if girls_count > max_girls_count:
        max_girls_count = girls_count
        max_girls_class = class_name
    if boys_count > max_boys_count:
        max_boys_count = max_boys_count
        max_boys_class = class_name
print(f'Больше всего мальчиков в классе {max_boys_class}')
print(f'Больше всего мальчиков в классе {max_girls_class}')




# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a