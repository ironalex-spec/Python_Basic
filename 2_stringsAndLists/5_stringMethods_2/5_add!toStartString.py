# На вход программе поступает строка. Ваша задача — дополнить ее впереди восклицательными знаками так,
#  чтобы длина строки стала равной 10 символам.

# Если на вход поступила строка, длина которой уже превысила 9 символов, то дополнять ее знаками ! не
#  нужно. Просто выведите строку в том виде, в котором она вводилась.

string1 = input()
print(string1.rjust(10,'!'))