# Вводится строка, которая может быть окружена символами -, _, !, ?

# Ваша задача убрать`все символы -, _, !, ? слева от строки и вывести полученный результат

string1 = input()
print(string1.lstrip('-_!?'))