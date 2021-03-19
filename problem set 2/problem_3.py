# Paste your code into this box
balance
annualInterestRate 
monthlyInterestRate = annualInterestRate / 12
minimum = balance / 12
maximum = (balance * (1 + monthlyInterestRate)**12) / 12.0
guess = (minimum + maximum)/2
remain = balance

precision = 0.10 

while (remain >= precision):
    guess= (minimum + maximum)/2
    for i in range (1,13):
        newBalance = remain - guess
        monthInterest = annualInterestRate/12*newBalance
        remain = newBalance+monthInterest
    if (remain < 0): #paying too much.... need to decrease the value
        maximum = guess
        remain = balance  # reset the remain to start again!!

    elif (remain > precision): #paying less .... need to increase the value
        minimum = guess
        remain = balance  # reset the remain to start again!!   

print("Lowest Payment: %.2f" %(guess))
