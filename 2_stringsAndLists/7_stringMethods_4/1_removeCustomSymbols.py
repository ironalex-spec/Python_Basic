# Вводится строка, которая может быть окружена символами -, _, !, ?
# Ваша задача избавиться от символов -, _, !, ? и вывести полученную строку

# Sample Input 1:

# -----Hello----
# Sample Output 1:

# Hello
# Sample Input 2:

# !!!World?????????
# Sample Output 2:

# World
# Sample Input 3:

# ___________Зачет!!!!!!!!
# Sample Output 3:

# Зачет
# Sample Input 4:

# !?!?!??!_---____-----qwerty
# Sample Output 4:

# qwerty

string1 = input()
print(string1.strip('-_!?'))