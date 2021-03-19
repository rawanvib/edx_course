# Paste your code into this box
balance
annualInterestRate
monthlyPaymentRate

for i in range(1,13):
    # calculate monthly income rate
    monthlyInterestRate=(annualInterestRate)/12.0
    
    # calculate minimum monthly payment
    minimumMonthlyPayment=monthlyPaymentRate*balance
    
    # calculate unpaid balance of the month
    unpaidBalance=balance-minimumMonthlyPayment
    
    #update the npaid balance
    updatedBalance=unpaidBalance+(monthlyInterestRate*unpaidBalance)
    
    updatedBalance=round(updatedBalance,2)
    
    balance=updatedBalance
    
print("Remaning balance: ",balance)

