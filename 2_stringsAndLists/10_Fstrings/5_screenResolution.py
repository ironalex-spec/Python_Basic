# Вам поступает на вход два натуральных числа - ширина экрана и его высота в пикселях. В результате на экране 
# разрешение экрана и общее количество пикселей в определенном формате. Все знаки препинания, пробелы, регистр 
# букв важны. Также обратите внимание, что в этом месте «1920 x 1080» стоит английская буква «x»

widthPx, heightPx = map(int, input().split())


print(f"Разрешение экрана: {widthPx} x {heightPx}.")
print(f"Общее количество пикселей = {widthPx * heightPx}.")