# Инициалы
# Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека

# Вам необходимо вывести фамилию и инициалы, как в примерах ниже

# Sample Input 1:

# Марина Денисовна Климова
# Sample Output 1:

# Климова М.Д.
# Sample Input 2:

# Марк Ильич Воробьев
# Sample Output 2:

# Воробьев М.И.

phrases = input()

print(f"{phrases.split()[2]} {phrases.split()[0][0]}.{phrases.split()[1][0]}.")