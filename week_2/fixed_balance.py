
def calcFinalBalance(balance,annualInterestRate, monthlyFixed):
	monthlyInterestRate = annualInterestRate/12
	month = 0
	while month < 12:
		monthlyUnpaid = balance - monthlyFixed
		monthlyUnpaid += (monthlyInterestRate*monthlyUnpaid)
		balance = monthlyUnpaid
		month += 1
	return balance

balance = 3926
annualInterestRate = 0.2
monthlyPayment = 10.00
finalBalance = 0.0

while finalBalance >= 0:
	finalBalance = calcFinalBalance(balance,annualInterestRate,monthlyPayment)
	if finalBalance <= 0:
		print("Lowest Payment: ",int(monthlyPayment))
		break
	else:
		monthlyPayment += 10


