# Paste your code into this box
balance 
annualInterestRate 
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance


while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        newbalance += (monthlyInterestRate * newbalance)
        month += 1    
print("Result Your Code Should Generate:\n")
  
print("-------------------")
print(" Lowest Payment:", monthlyPayment)
