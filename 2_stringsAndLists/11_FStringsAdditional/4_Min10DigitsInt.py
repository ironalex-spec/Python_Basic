# Вводится целое число, необходимо вывести его на экран, отведя как минимум 10 разрядов 
# под отображение числа. Если в числе не хватает разрядов, необходимо выводить незначащие нули

intDigit = int(input())
print(f"{intDigit:010d}")