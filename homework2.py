# П, К и С делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что П и С сделали 
# одинаковое количество журавликов, а К сделала в два раза больше журавликов, чем П и С вместе.

number = int(input('Введите число сделанных журавликов: '))
s = number // 6
p = number // 6
k = (number // 6) * 4

print(s, k, p)