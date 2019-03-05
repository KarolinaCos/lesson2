# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
name_dict = {}
for tmp_dict in students:
  pupil_name = tmp_dict["first_name"]
  if pupil_name in name_dict.keys():
    name_dict[pupil_name] += 1
  else:
    name_dict[pupil_name] = 1

for pupil_name in name_dict.keys():
  print(pupil_name, "=" , name_dict[pupil_name])
 
 
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students_second = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
def find_max_list(list_in):
  name_dict = {}
  for tmp_dict in list_in:
    pupil_name = tmp_dict["first_name"]
    if pupil_name in name_dict.keys():
      name_dict[pupil_name] += 1
    else:
      name_dict[pupil_name] = 1

  list_of_value = name_dict.values()
  max_value = max(list_of_value)
  for name in name_dict.keys():
    if name_dict[name] == max_value:
      print("Most frequently name =", name)

find_max_list(students_second)



# Пример вывода:
# Самое частое имя среди учеников: Маша

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
print("====")
print("Class_1")
find_max_list(school_students[0])
print("Class_2")
find_max_list(school_students[1])





# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


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

def count_sex_in_class(list_in):
  boys_number = 0
  girls_number = 0
  for name in list_in:
    if is_male[name]:
      boys_number += 1
    else:
      girls_number += 1
  return (boys_number, girls_number)  

def sex_in_the_class(dict_in):
  pupils_list = dict_in["students"] 
  names_only = []
  for dict_name in pupils_list:
    names_only.append(dict_name["first_name"])
  #count_sex_in_class(names_only)
  boys, girls = count_sex_in_class(names_only)
  message = "boys = " + str(boys) + ' ' + "girls = " + str(girls)
  return message
  #print(count_sex_in_class(names_only))


""" test_list = ["Маша", "Оля"]
print(count_sex_in_class(test_list))   """

print("=========================")
print("class 2a:", sex_in_the_class(school[0]))
print("class 3c:", sex_in_the_class(school[1]))


#sex_in_the_class(school[1]) 


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
def define_popular_sex_in_class(list_in):
  boys_number = 0
  girls_number = 0
  for name in list_in:
    if is_male[name]:
      boys_number += 1
    else:
      girls_number += 1
  if boys_number > girls_number:
    return("more boys")
  elif girls_number > boys_number:
    return("more girls")
  else:
    return("equal")

def popular_sex_in_dict_class(dict_in):
  pupils_list = dict_in["students"] 
  names_only = []
  for dict_name in pupils_list:
    names_only.append(dict_name["first_name"])
  #return names_only
  message = define_popular_sex_in_class(names_only)
  return message

print("========================")

print("In class 2a is", popular_sex_in_dict_class(school[0]))
print("In class 3c is", popular_sex_in_dict_class(school[1]))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a