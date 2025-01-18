# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество минут и секунд при необходимости дополняются до двузначного числа нулями.

# Программа получает на вход число n - количество секунд, которое прошло с начала суток.

# Выведите показания часов, соблюдая формат.

secondPass = int(input())

hour = secondPass // 3600
secondPass = secondPass % 3600

minute = secondPass // 60
secondPass = secondPass % 60

print(hour,':',minute // 10, minute % 10, ':',secondPass // 10, secondPass % 10, sep='')