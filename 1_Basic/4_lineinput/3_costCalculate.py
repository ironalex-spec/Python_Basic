# Известно, что на обработку одного квадратного метра панели требуется 1г сульфида. 
# Всего необходимо обработать N прямоугольных панелей размером A на B метров.
# Вам необходимо подсчитать, сколько всего сульфида необходимо на обработку всех панелей. 
# И не забудьте, что панели требуют обработки с обеих сторон.

# На вход программе подаются 3 положительных целых числа N,A,B в одну строку

# PS: в этой задаче обратите внимание на формат ввода. Числа вводятся в одну строку, поэтому вы уже не можете их так считать:

# n = int(input())
# a = int(input())
# b = int(input())

# Возникнет ошибка! Чтобы считать три значения, которые поступают через пробел в одной строке, пользуйтесь следующей инструкцией:

# n, a, b = map(int, input().split()) 

n, a, b = map(int, input().split())
squareSulfideNeed = 1
cost = a * b * n * 2 * squareSulfideNeed
print(cost)
