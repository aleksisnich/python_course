# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
# print(‘ok’)
# else:
# print(‘fail’)
# Вывод:
# ok


# transformation = lambda x: x

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(lambda x: x, values))


# print(transormed_values == values



# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_orbits):
#     max_square = 0
#     max_element = list_orbits[0]
#     for element in list_orbits:
#         for j in range(1):
#             if element[j] != element[j + 1] and max_square < element[j] * element[j + 1]:
#                 max_square = element[j] * element[j + 1]
#                 max_element = element
#     return max_element            

# print(*find_farthest_orbit(orbits))

# Через словариL:
# def ﬁnd_farthest_orbit(list_of_orbits):
#     dict_s_orbits = {3.14 * orbit[0] * orbit[1]: orbit for orbit in list_of_orbits if orbit[0] != orbit[1]}
#     return dict_s_orbits[max(dict_s_orbits)]

# Через лямбда функцию:
# def ﬁnd_farthest_orbit(list_of_orbits):
#     return max(filter(lambda x: x[0] != x[1], list_of_orbits), key=lambda x: 3.14 * x[0] * x[1])


#   HOMEWORK №1
# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# По умолчанию номер столбца и строки = 9. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!. 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения. Между элементами должен быть 1 пробел, в конце строки пробел не нужен.


# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for i in range(1, num_columns + 1):
#             for j in range(1, num_rows + 1):
#                 if j != num_rows:
#                     print(operation(i, j), end = ' ')
#                 else:
#                     print(operation(i, j))      
    
# print_operation_table(lambda x, y: x * y, 1, 3)




# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
# В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: 
# Количество фраз должно быть больше одной!


# stroka = 'пара-ра-рам парарарам'
# new_stroka = stroka.split()
# letters = 'ауоыиэяюёеАУОЫИЭЯЮЁЕ'
# count = 0
# calc = 0
# string = ''
# check = []

# if len(new_stroka) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     for i in range(len(new_stroka)):
#         string = new_stroka[i]
#         for j in string:
#             if j in letters:
#                 count += 1
#         check.append(count)
#         count = 0
    
#     for i in range(len(check) - 1):
#         if check[i] != check[i+1]:
#             print('Пам парам')
#             break
#         else:
#             calc += 1
        
#     if calc == (len(check)-1):
#         print('Парам пам-пам')
            
            

    





