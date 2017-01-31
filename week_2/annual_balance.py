balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
while month < 12:
	monthlyInterestRate = annualInterestRate/12
	minMonthlyPayment = monthlyPaymentRate*balance
	monthlyUnpaidBalance = balance - minMonthlyPayment
	updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
	balance = updatedBalance
	month += 1
print("Remaining balance ",round(balance,2))