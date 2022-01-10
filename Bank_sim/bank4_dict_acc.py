# Non-OOP
# Bank Version 1
# Single account

accountsList = []

def newAccount(name, balance, password):
    global accountsList
    newAccountDict = {'name':name,'balance':balance,'password':password}
    accountsList.append(newAccountDict)  

def show(accountNumber):
    global accountsList
    print('Account: ', accountNumber)
    thisAccountDict = accountsList[accountNumber]
    print('     Name: ', thisAccountDict['name'])
    print('     Balance: ', thisAccountDict['balance'])
    print('     Password: ', thisAccountDict['password'])
    print()

def getBalance(accountNumber, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if password != thisAccountDict['password']:
            print('Incorrect password')
            return None
    return thisAccountDict['balance']

def deposit(accountNumber, amountToDeposit, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToDeposit < 0:
            print('You cannot deposit  a negative amount!')
            return None
    if password != thisAccountDict['password']:
            print('Incorrect password')
            return None

    thisAccountDict['balance'] = thisAccountDict['balance'] + amountToDeposit
    return thisAccountDict['balance']

def withdraw(accountNumber, amountToWithdraw, password):
    global accountsList
    thisAccountDict = accountsList[accountNumber]
    if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount!')
            return None

    if password != thisAccountDict['password']:
            print('Incorrect password')
            return None

    if amountToWithdraw > thisAccountDict['balance']:
            print('You cannot withdraw more than you have in your account')
            return None

    thisAccountDict['balance'] = thisAccountDict['balance'] - amountToWithdraw
    return thisAccountDict['balance']


# Create two sample accounts
print("Joe's account is account number:", len(accountsList))
newAccount("Joe", 100, 'soup')
print("Mary's account is account number:", len(accountsList))
newAccount("Mary", 12345, 'nuts')

while True:
    print()
    print('Press b to get the balance')
    print('Press d to make a deposite')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quite')
    print()

    action = input('What do you want to do? ')
    action = action.lower() #force lowercase
    action = action[0]
    print()

    if action == 'b':
        print('Get Balance:')

        userAccountNumber = int(input('Please enter your accountnumber: '))
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userAccountNumber,userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')

        userAccountNumber = int(input('Please enter your accountnumber: '))
        userDepositAmount = input('Please enter amount to deposit: ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password: ')

        newBalance = deposit(userAccountNumber,userDepositAmount, userPassword)
        if theBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 'w':
        print('Withdraw:')

        userAccountNumber = int(input('Please enter your accountnumber: '))
        userWithdrawAmount = input('Please enter the amount to withdraw: ')
        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter the password: ')

        newBalance = withdraw(userAccountNumber,userWithdrawAmount, userPassword)
        if theBalance is not None:
            print('Your new balance is:', newBalance)
        else:
            print('Your new balance is: 0')
    
    elif action == 's':
        userAccountNumber = int(input('Please enter your accountnumber: '))
        show(userAccountNumber)

    else: 
        break

print('Done')
            

        

    