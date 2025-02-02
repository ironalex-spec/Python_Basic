# Напишите программу для перевода натурального значения секунд в значение минут определенного формата.

# Sample Input 1:

# 99
# Sample Output 1:

# 99 сек - это 1 мин. 39 сек.
# Sample Input 2:

# 123
# Sample Output 2:

# 123 сек - это 2 мин. 3 сек.



seconds = int(input())

chMinutes = seconds // 60
chSeconds = seconds % 60

print(f"{seconds} сек - это {chMinutes} мин. {chSeconds} сек.")
