
def deposit():
    while True:
        amount = input("What would you like to input (Cash/Coin): ").title()
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number!")

    return deposit

def main():
    balance = deposit()
    print(balance)
main()
