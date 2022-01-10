# Test program using accounts
# Version 3, using a dictionary of accounts
# Bring in all the code from the Account class file
from Account import *

accountsDict = {} 
nextAccountNumber = 0 
# Create two accounts:
oAccount = Account('Joe', 100, 'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount 


nextAccountNumber = nextAccountNumber + 1 
oAccount = Account('Mary', 12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
nextAccountNumber = nextAccountNumber + 1

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposite')
    print('Press o to open an account')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quite')
    print()

    action = input('What do you want to do? ')
    action = action.lower() #force lowercase
    action = action[0]
    print()

    if action == 'b':
        print('****Get Balance*****')

        userAccountNumber = int(input('Please enter your accountnumber: '))
        userAccountPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.getBalance(userAccountPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)
    
    elif action == 'd': 
        print('*** Deposit ***')
        userAccountNumber = input('Please enter the account number: ')
        userAccountNumber = int(userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber] 
        theBalance = oAccount.deposit(userDepositAmount, userPassword)

        if theBalance is not None:
            print('Your new balance is:', theBalance)
    
    elif action == 'o':
        print('*** Open Account ***')
        userName = input('What is the name for the new user account? ')
        userStartingAmount = input('What is the starting balance for this account? ')
        userStartingAmount = int(userStartingAmount)
        userPassword = input('What is the password you want to use for this account? ')
        oAccount = Account(userName, userStartingAmount, userPassword)
        accountsDict[nextAccountNumber] = oAccount
        print('Your new account number is:', nextAccountNumber)
        nextAccountNumber = nextAccountNumber + 1
        print()

    elif action == 's':
        print('Show:')
        for userAccountNumber in accountsDict:
            oAccount = accountsDict[userAccountNumber]
            print(' Account number:', userAccountNumber)
            oAccount.show()

    elif action == 'q':
        break

    elif action == 'w':
        print('*** Withdraw ***')
        userAccountNumber = input('Please enter your account number: ')
        userAccountNumber = int(userAccountNumber)
        userWithdrawalAmount = input('Please enter the amount to withdraw: ')
        userWithdrawalAmount = int(userWithdrawalAmount)
        userPassword = input('Please enter the password: ')
        oAccount = accountsDict[userAccountNumber]
        theBalance = oAccount.withdraw(userWithdrawalAmount,
        userPassword)
        if theBalance is not None:
            print('Withdrew:', userWithdrawalAmount)
            print('Your new balance is:', theBalance)

    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
