
def calcFinalBalance(balance,annualInterestRate, monthlyFixed):
	monthlyInterestRate = annualInterestRate/12
	month = 0
	while month < 12:
		monthlyUnpaid = balance - monthlyFixed
		monthlyUnpaid += (monthlyInterestRate*monthlyUnpaid)
		balance = monthlyUnpaid
		month += 1
	return balance
def calcHigh(balance,monthlyInterestRate):
	return (balance*(1+monthlyInterestRate)**12)/12
def getMax(balance,annualInterestRate,monthlyPayment,high,low):
	new_balance = calcFinalBalance(balance,annualInterestRate,monthlyPayment)
	while new_balance > 0:
		high = high + monthlyPayment
		monthlyPayment = round(((high+low)/12),2)
		new_balance = calcFinalBalance(balance,annualInterestRate,monthlyPayment)
	return ((high+low)/12)



balance = 3926
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
high = calcHigh(balance,monthlyInterestRate)
low = balance/12
monthlyPayment = (high+low)/12
high = getMax(balance,annualInterestRate,monthlyPayment,high,low)
low = (high+low)/2
count=0
while count < 30000:
	monthlyPayment = (high+low)/2
	new_balance = calcFinalBalance(balance,annualInterestRate,monthlyPayment)
	count += 1
	if new_balance > 0:
		low = monthlyPayment
	elif new_balance < -0.1:
		high = monthlyPayment
	else:
		print("Lowest Payment ",round(((high+low)/2),2))
		break


