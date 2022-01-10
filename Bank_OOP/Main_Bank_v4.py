# Main program for controlling a Bank made up of Accounts
# Bring in all the code of the Bank class

from Bank import *
# Create an instance of the Bank
oBank = Bank('9 to 5', '123 Main Street, Anytown, USA', '(650) 555-1212')

# Main code
# Create two test accounts
joesAccountNumber = oBank.createAccount('Joe', 100,'JoesPassword')
print("Joe's account number is:", joesAccountNumber)
marysAccountNumber = oBank.createAccount('Mary', 12345,'MarysPassword')
print("Mary's account number is:", marysAccountNumber)

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank information, press i')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w')
    print()


    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0] # grab the first letter
    print()

    try:
        if action == 'b':
            oBank.balance()

        elif action == 'c':
            oBank.closeAccount()

        elif action == 'd':
            oBank.deposit()

        elif action == 'o':
            oBank.openAccount()

        elif action == 's':
            oBank.show()

        elif action == 'q':
            break

        elif action == 'w':
            oBank.withdraw()
        elif action == 'i':
            oBank.getInfo()

    except AbortTransaction as error:
        print(error)

print('Done')
