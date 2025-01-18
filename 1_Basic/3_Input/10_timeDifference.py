# ; Даны значения двух моментов времени, принадлежащих одним и тем же суткам: часы, минуты и секунды для каждого из моментов времени. Известно, что второй момент времени наступил не раньше первого.
#  Определите, сколько секунд прошло между двумя моментами времени.

# Программа на вход получает три целых числа: часы, минуты, секунды,
#  задающие первый момент времени и три целых числа, задающих второй момент времени.

iHour1 = int(input())
iMinute1 = int(input())
iSecond1 = int(input())
iHour2 = int(input())
iMinute2 = int(input())
iSecond2 = int(input())

timeDifference = (iHour2 - iHour1) * 3600 + (iMinute2 - iMinute1) * 60 + (iSecond2 - iSecond1)

print(timeDifference) 
