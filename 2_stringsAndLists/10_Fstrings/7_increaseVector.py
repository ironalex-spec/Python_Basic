# Нашей программе поступает на вход x, y, z - три целых числа, обозначающие координаты вектора А. Затем необходимо найти 
# координаты вектора B, путем увеличения на 5 каждой из координаты вектора А.

# Оба вектора необходимо распечатать в определенном формате

int1 = int(input())
int2 = int(input())
int3 = int(input())

print(f"Vector A({int1}, {int2}, {int3})")
print(f"Vector B({int1 + 5}, {int2 + 5}, {int3 + 5})")