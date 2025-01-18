# У Олега в банке есть n евро. Он хочет снять всю сумму наличными. 
# Номиналы еврокупюр равны 1, 5, 10, 20, 100. 
# Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
# На вход программе поступает одно положительные целое число n.

bankDeposit = int(input())

handredNum = bankDeposit // 100
bankDeposit = bankDeposit % 100

twentyNum = bankDeposit // 20
bankDeposit = bankDeposit % 20

tenNum = bankDeposit // 10
bankDeposit = bankDeposit % 10

fiveNum = bankDeposit // 5
bankDeposit = bankDeposit % 5

oneNum = bankDeposit // 1

print(handredNum + twentyNum + tenNum + fiveNum + oneNum)