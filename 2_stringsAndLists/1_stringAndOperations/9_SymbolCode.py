#  Программа принимает на вход три символа через пробел в одну строку.
# Необходимо вывести код каждого символа при помощи функции ord в определенном формате.

char1, char2, char3 = map(str, input().split())
print('Simvol code ' + char1 + ' is ' + str(ord(char1)) + '.')
print('Simvol code ' + char2 + ' is ' + str(ord(char2)) + '.')
print('Simvol code ' + char3 + ' is ' + str(ord(char3)) + '.')
