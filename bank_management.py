# ==========================================
#       BANK MANAGEMENT SYSTEM
# ==========================================

accounts = {}

# Function to create new account
def create_account():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists!")
    else:
        name = input("Enter Customer Name: ")
        acc_type = input("Enter Account Type (Saving/Current): ")

        balance = float(input("Enter Initial Balance: "))

        accounts[acc_no] = {
            "name": name,
            "type": acc_type,
            "balance": balance
        }

        print("Account Created Successfully!")


# Function to deposit money
def deposit_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Deposit Amount: "))

        if amount > 0:
            accounts[acc_no]["balance"] += amount
            print("Amount Deposited Successfully!")
            print("Updated Balance:", accounts[acc_no]["balance"])
        else:
            print("Invalid Amount!")
    else:
        print("Account Not Found!")


# Function to withdraw money
def withdraw_money():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        amount = float(input("Enter Withdraw Amount: "))

        if amount <= accounts[acc_no]["balance"]:
            accounts[acc_no]["balance"] -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance:", accounts[acc_no]["balance"])
        else:
            print("Insufficient Balance!")
    else:
        print("Account Not Found!")


# Function to check balance
def check_balance():
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("\n===== ACCOUNT DETAILS =====")
        print("Customer Name :", accounts[acc_no]["name"])
        print("Account Number:", acc_no)
        print("Account Type  :", accounts[acc_no]["type"])
        print("Current Balance:", accounts[acc_no]["balance"])
    else:
        print("Account Not Found!")


# Function to transfer money
def transfer_money():
    sender = input("Enter Sender Account Number: ")
    receiver = input("Enter Receiver Account Number: ")

    if sender in accounts and receiver in accounts:

        amount = float(input("Enter Transfer Amount: "))

        if amount <= accounts[sender]["balance"]:

            accounts[sender]["balance"] -= amount
            accounts[receiver]["balance"] += amount

            print("Money Transferred Successfully!")

        else:
            print("Insufficient Balance!")

    else:
        print("One or Both Accounts Not Found!")


# Function to view all accounts
def view_all_accounts():

    if len(accounts) == 0:
        print("No Accounts Available!")

    else:
        print("\n======= ALL ACCOUNTS =======")

        for acc_no, details in accounts.items():

            print("\nAccount Number :", acc_no)
            print("Customer Name  :", details["name"])
            print("Account Type   :", details["type"])
            print("Balance        :", details["balance"])


# Function to delete account
def delete_account():

    acc_no = input("Enter Account Number to Delete: ")

    if acc_no in accounts:
        del accounts[acc_no]
        print("Account Deleted Successfully!")
    else:
        print("Account Not Found!")


# Main Program
while True:

    print("\n========== BANK MANAGEMENT SYSTEM ==========")
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transfer Money")
    print("6. View All Accounts")
    print("7. Delete Account")
    print("8. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        check_balance()

    elif choice == "5":
        transfer_money()

    elif choice == "6":
        view_all_accounts()

    elif choice == "7":
        delete_account()

    elif choice == "8":
        print("Thank You For Using Bank Management System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")
