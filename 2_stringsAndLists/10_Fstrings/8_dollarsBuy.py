# Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число), которое 
# пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:

# Current dollar rate is <курс доллара>. You want to buy <количество долларов> dollars
# You must pay <стоимость>

dollarCost = float(input())
intNumDollars = int(input())

print(f"Current dollar rate is {dollarCost}. You want to buy {intNumDollars} dollars")
print(f"You must pay {dollarCost * intNumDollars}")