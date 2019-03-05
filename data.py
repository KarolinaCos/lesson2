# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name)


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in names:
    print(name, len(name))



# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
for name in is_male.keys():
    if is_male[name]:
        print(name, "Man")
    else:
        print(name, "Woman")


# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print("number_of_groups =", len(groups))
number1 = 0
for pupils in groups[0]:
  number1 = number1 + 1
print("pupils_class_1 =", number1)

number2 = 0
for pupils in groups[1]:
  number2 = number2 + 1
print("pupils_class_2 =", number2)




# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

class_one = '' 
for pupil in groups[0]:
  class_one = class_one + ' ' + pupil
print("pupils_class_1 =", class_one)

class_two = ''
for pupil in groups[1]:
 class_two = class_two + ' ' + pupil
print("pupils_class_2 =", class_two)

