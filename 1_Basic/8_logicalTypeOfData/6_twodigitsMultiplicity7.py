# На вход программе поступают два целых числа в одной строке.

# Программа должна вывести True, если оба числа делятся на 7, в противном случае - False.

# Сделать задачу необходимо без использования условного оператора.

x1, x2 = map(int, input().split())
print(x1 % 7 == 0 and x2 % 7 == 0)