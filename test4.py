# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (иногда с хвоста). 
# В каждом вагоне написан его номер. Витя сел в i-ый вагон от головы поезда с номером j. 
# Сколько всего вагонов? 

number_head = int(input('Введите номер вагона от головы: '))
number_current = int(input('Введите текущий номер вагона: '))

if number_head != number_current:
    wagons = number_head + (number_current - 1)
    print('Количество вагонов: ', wagons)
else:
    print('Невозможно определить количество вагонов :(')

    
    
