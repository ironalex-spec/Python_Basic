# Программа запрашивает у пользователя имя и фамилию, после чего выводит приветственное сообщение в следующем формате «Здравствуйте, <фамилия> <имя>!»

# Sample Input 1:

# Петя
# Иванов
# Sample Output 1:

# Здравствуйте, Иванов Петя!
# Sample Input 2:

# Никита
# Рассказов
# Sample Output 2:

# Здравствуйте, Рассказов Никита!

strName = input()
strLastName = input()
print("Здравствуйте, {lastName} {firstName}!".format(lastName=strLastName,
                                                    firstName=strName))
