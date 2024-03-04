import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C':6,
    'D':8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        #[:] tp create a copy
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(all_symbol)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns 

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()

# Get the deposit amount
def deposit():
    while True:
        amount = input("What would you like to input: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number!")

    return amount

# Get number of line for betting
def get_number_of_line():
        while True:
            lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print("Enter a valid number of line: ")
            else:
                print("Please enter a number!")
        return lines

# Amount to bet on between min and max bet
def get_bet():
        while True:
            amount = input("What would you like to bet on each line: ")
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
            else:
                print("Please enter a number!")
        return amount

# return the value from the previous function to balance and lines
# print the amount of bet on what line and total bet
def main():
    balance = deposit()
    lines = get_number_of_line()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if balance < total_bet:
            print(f"Insufficient Fund, you current balance is {balance}")
        else:
            break
        
    print(f"Your betting is ${bet} on {lines} line. Total bet is equal to ${total_bet}.\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main() 
