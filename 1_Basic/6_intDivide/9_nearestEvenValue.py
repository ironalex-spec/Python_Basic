# Дано целое число n. Выведите следующее за ним четное число.
# Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.

n = int(input())
intDivide = n // 2
print((intDivide + 1) * 2)