# В некоторой школе решили набрать три новых математических класса и оборудовать 
# кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
#  Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
#  которое нужно приобрести для них. 
import math

class1 = int(input())
class2 = int(input())
class3 = int(input())
print(math.ceil(class1/2) + math.ceil(class2/2) + math.ceil(class3/2))