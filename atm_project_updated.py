# - register
# - firstname, lastname, password, email
# - generation user account
# - login
# - account number and password

#Initializing the system
import random

database = {
    7259196222: ['ade', 'Adde', 'ade@you.co', 'aaaa']
} #dictionary

account_balance = 450
deposit_amount = 0
withdrawal_amount =0

def init():

    print("Welcome to adexBank")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()


#bank operations

def login():

    print("*********** Login ************")

    enterAccdetails = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == enterAccdetails):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print("Invalid account or password")
    login()

    

def generationAccountNumber():
    return random.randrange(1111111111,9999999999)

def register():
    print("******** Register **********")
    email = input("What is your email address? \n")
    first_name = input("What is your firstname? \n")
    last_name = input("what is your lastname? \n")
    password = input("Create Your Password \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your account has been created")
    print("==== ===== ======= ======== ============")
    print("Your account number is: %d" %accountNumber)
    print("Make sure you keep it safe")
    print("=============  ==============  =========")

    login()

def bankOperation(user):
    print("Welcome %s %s" % ( user[0], user[1]))

    selectedOption = int(input("What would you like to do? (1) deposit (2) withdrawal (3) balance (4) Logout (5) Exit \n"))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):            
        withdrawalOperation()
    elif(selectedOption == 3):             
        getCurrentBalance() 
    elif(selectedOption == 4):             
        logout()
    elif(selectedOption == 5):            
        exit()
    else:            
        print("Invalid option selected")
    bankOperation(user)

def getCurrentBalance():
    print("Your current balance: ", account_balance)

def withdrawalOperation():
    withdrawal_amount = float(input("How much would you like to withdraw today?\n")) 
    if withdrawal_amount > account_balance:                                     
        print("Insuffient funds, N%.2f is greater than your account balance of N%.2f" % (withdrawal_amount, account_balance)) 
    else:                                                                        
        balance = account_balance - withdrawal_amount                               
        print ("Withdrawal amount was N%.2f, your new current balance is N%.2f" % (withdrawal_amount, balance))  
    
def depositOperation():
    deposit_amount = float(input("How much would you like to deposit today?\n"))  
    balance = account_balance + deposit_amount                                    
    print("Deposit was N%.2f , your new current balance is N%.2f" % (deposit_amount, balance))

def logout():
    login()



##Actual Banking System ####

init()
