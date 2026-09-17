accounts = {
    "SURAJ123": {
        "acc_num": 123,
        "user_id": "suraj",
        "balance": 0
    },
    "VINAY123":{
        "acc_num": 456,
        "user_id": "vinay",
        "balance": 0
    },
    "YOGITA123":{
        "acc_num": 789,
        "user_id": "yogita",
        "balance": 0
    },
    "REVATI123":{
        "acc_num": 000,
        "user_id": "revati",
        "balance": 0
    }
}


def show_balance(account):
    print(f"user_name is: {account["user_id"]}")
    print(f"balance is {account["balance"]}")

def withdraw(account, amount):
    account["balance"] -= amount

def deposite(account, amount):
    account["balance"] += amount

def show_menu():
    print("\n===== SIMPLE BANK =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        deposite_amt = float(input("enter amount: "))
        deposite(accounts["REVATI123"], deposite_amt)
    elif choice == '2':
        withdraw_amt = float(input("enter amount: "))
        withdraw(accounts["REVATI123"], withdraw_amt)
    elif choice == '3':
        show_balance(accounts["REVATI123"])
    else:
        break




