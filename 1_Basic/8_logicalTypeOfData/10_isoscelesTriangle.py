# На вход поступают три целых числа - стороны треугольника.

# Необходимо вывести True, если данные стороны образуют равнобедренный треугольник, в противном случае - False.

# Сделать задачу необходимо без использования условного оператора.

a, b, c = map(int, input().split())
print((a == b) or (a == c) or (b == c))