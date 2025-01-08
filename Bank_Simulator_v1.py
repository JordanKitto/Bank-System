user_account = {"pin": 0, "Account Name": "", "Account_number": 0, "Balance": 0}

user_status = {"status": False}

def create_accountNo():
    while True:
        try:
            user_input = int(input("Please enter an 4 digit account number: "))
            if 1000 <= user_input <= 9999:
                user_account.update(Account_number=user_input)
                print(f"Account number {user_account['Account_number']} Successful created!")
                break
            else:
                print("Invalid account number, enter a 4 digit account number")
        except ValueError:
            print("Account number can only be numerical values 1- 9")
    while True:
        try:
            user_input = int(input("Enter a 4-digit PIN number: "))
            if 1000 <= user_input <= 9999:
                print("Pin Successfully set!")
                user_account.update(pin=user_input)
                print(user_account["pin"])
                main_function()
                break
            else:
                print("Invalid PIN. Must be 4 digits")
        except ValueError:
            print("PIN must be numeric")

def login():
    while True:
        try:
            user_input = int(input("Please enter your account number: "))
            if user_input == user_account["Account_number"]:
                print(f"Account number {user_account['Account_number']} confirmed")
                break
            else:
                print("Invlaid account number")
                user_input = int(input("Please enter your account number: "))
        except ValueError:
            print("Enter numberical values only")
        
    while True:
        try:
            user_input = int(input("Please enter your pin: "))
            if user_input == user_account["pin"]:
                user_status.update(status=True)
                print(f"Account pin confirmed")
                Display_Account()
                break
            else:
                print("Invlaid pin")
                user_input = int(input("Please enter your pin: "))
        except ValueError:
            print("Enter numerical values only")


def Status():
    if user_status["status"] == True:

        print(f"Account {user_account['Account_number']} is logged in")
        main_function()

    else:
        print("No account found! "'\n' "Would you like to login or sign up ?")
    while True:
            print("1. Login")
            print("2. Sign up")
            try:
                user_input = int(input("Choose an option: "))
                if user_input == 1:
                    print("---Login---")
                    login()
                    break
                else:
                    print("---Account Creation---")
                    create_accountNo()
                break
            except ValueError:
                print("Enter numerical values only")

def Display_Balance():
    print(f"Your balance is: $ {user_account["Balance"]}")
    input("Press enter to return home")
    Display_Account()
        
def Deposit_Money():
    while True:
        print("1. Deposit $10")
        print("2. Deposit $20")
        print("3. Deposit $50")
        print("4. Deposit $100")
        print("5. Deposit x")
        try:
            user_input = int(input("Select deposit option: "))
            if user_input == 1:
                user_account.update(Balance=user_input + 10)
                Display_Account()
                break
            elif user_input == 2:
                user_account["Balance"] = user_account["Balance"] + 20
                Display_Account()
                break
            elif user_input == 3:
                user_account["Balance"] = user_account["Balance"] + 50
                Display_Account()
                break
            elif user_input == 4:
                user_account["Balance"] = user_account["Balance"] + 100
                Display_Account()
                break
            elif user_input == 5:
                deposit_amount = int(input("Enter deposit amount: $"))
                user_account["Balance"] = deposit_amount + user_account["Balance"]
                Display_Account()
                break
            else:
                print("Invlaid option")
                user_input = int(input("Please try again: "))
        except ValueError:
            print("Enter numerical values only")

def Withdraw_Money():
    while True:
        print("1. Withdraw $ 10")
        print("2. Withdraw $ 20")
        print("3. Withdraw $ 50")
        print("4. Withdraw $ 100")
        print("5. Withdraw x")
        try:
            user_input = int(input("Select withdraw amount: "))
            if user_input == 1:
                user_account["Balance"] = user_account["Balance"] - 10
                Display_Account()
                break
            elif user_input == 2:
                user_account["Balance"] = user_account["Balance"] - 20
                Display_Account()
                break
            elif user_input == 3:
                user_account["Balance"] = user_account["Balance"] - 50
                Display_Account()
                break
            elif user_input == 4:
                user_account["Balance"] = user_account["Balance"] - 100
                Display_Account()
                break
            elif user_input == 5:
                wihtdraw_amount = int(input("Enter amount to withdraw: $"))
                user_account["Balance"] = wihtdraw_amount - user_account["Balance"]
                Display_Account()
                break
            elif user_input > user_account["Balance"]:
                print("Insufficient funds")
                Display_Account()
            else:
                print("Invalid option")
                user_input = int(input("Please try again: "))
        except ValueError:
            print("Enter numerical values only")

def Transfer_Money():
    pass

def main_function():
    while True:
        print("1. Create account")
        print("2. Login")
        print("3. Check Status")
        print("4. Shutdown")
        try:
            user_input = int(input("Please Choose from the options below: "))
            if user_input == 1:
                create_accountNo()
                break
            elif user_input == 2:
                login()
                break
            elif user_input == 3:
                Status()
                break
            elif user_input == 4:
                print("Good Bye")
                break
            elif user_input <= 5:
                print("Invalid option")
        except ValueError:
            print("Numerical values only!")


def Display_Account():
    while True:
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Logout")

        try:
            user_input = int(input("Please choose an option below: "))
            if user_input == 1:
                Display_Balance()
                break
            elif user_input == 2:
                Deposit_Money()
                break
            elif user_input == 3:
                Withdraw_Money()
                break
            elif user_input == 4:
                print("Transfer Money")
                break
            elif user_input == 5:
                print("Log out")
                main_function()
                break
        except ValueError:
            print("Numerical values only!")
            user_input = int(input("Please Choose from the options below: "))


main_function()
