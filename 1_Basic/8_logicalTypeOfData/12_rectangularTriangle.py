# На вход поступают три целых числа - стороны треугольника.

# Необходимо вывести True, если данные стороны образуют прямоугольный треугольник, в противном случае - False.

# Для написания программы необходимо вспомнить теорему Пифагора

# Сделать задачу необходимо без использования условного оператора.

a, b, c = map(int, input().split())
print((a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == a**2 + b**2))