import random  # Import random module for random selection of slot machine symbols

# Declaring constants for the game
MAX_LINES = 3  # Maximum number of lines the player can bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1  # Minimum bet per line
ROWS = 3  # Number of rows in the slot machine grid
COLS = 3  # Number of columns in the slot machine grid

# Dictionary defining the number of each symbol in the slot machine
symbol_count = {
    "A": 2,  # 'A' appears twice in the slot machine
    "B": 4,  # 'B' appears four times
    "C": 6,  # 'C' appears six times
    "D": 8   # 'D' appears eight times
}

# Dictionary defining the value of each symbol when it appears in a winning line
symbol_value = {
    "A": 5,  # 'A' pays 5x the bet amount
    "B": 4,  # 'B' pays 4x the bet amount
    "C": 3,  # 'C' pays 3x the bet amount
    "D": 2   # 'D' pays 2x the bet amount
}

def check_winnings(columns, lines, bet, values):
    
    # Checks if there are winning lines in the slot machine spin.
    
    winnings = 0  # Total winnings
    winning_lines = []  # Stores the indices of winning lines
    
    for line in range(lines):  # Loop through the lines the player is betting on
        symbol = columns[0][line]  # Get the first symbol in the line
        is_winning_line = True  # Assume it's a winning line until proven otherwise

        for column in columns:  # Check if all columns have the same symbol in the current row
            if column[line] != symbol:
                is_winning_line = False  # If a mismatch is found, mark it as not a winning line
                break  # Stop checking further

        if is_winning_line:  # If all symbols in the line match
            winnings += values[symbol] * bet  # Multiply the symbol's value by the bet amount
            winning_lines.append(line + 1)  # Store the winning line (1-based index)

    return winnings, winning_lines  # Return total winnings and the winning lines

def get_slot_machine_spin(rows, cols, symbols):
    """
    Generates a random slot machine spin based on available symbols.
    :param rows: Number of rows in the slot machine.
    :param cols: Number of columns in the slot machine.
    :param symbols: Dictionary of symbol occurrences.
    :return: A 2D list representing the slot machine columns.
    """
    all_symbols = []  # List to store all symbols based on their frequency
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)  # Add each symbol to the list 'count' times

    columns = []  # List to store the randomly generated columns
    for _ in range(cols):  # Generate each column
        column = []
        current_symbols = all_symbols[:]  # Copy of all symbols to prevent repetition errors

        for _ in range(rows):  # Generate each row in the column
            value = random.choice(current_symbols)  # Select a random symbol
            current_symbols.remove(value)  # Remove it to avoid duplicates in the same column
            column.append(value)

        columns.append(column)  # Add the completed column to the slot machine

    return columns  # Return the slot machine columns

def print_slot_machine(columns):
    """
    Prints the slot machine spin in a formatted way.
    :param columns: The 2D list representing the slot machine's columns.
    """
    for row in range(len(columns[0])):  # Iterate through rows
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # Print with separator
            else:
                print(column[row], end="")  # Last column without separator
        print()  # Move to the next line after printing a row

def deposit():
    """
    Prompts the user to enter the deposit amount.
    :return: Valid deposit amount.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():  # Check if input is a number
            amount = int(amount)
            if amount > 0:
                return amount  # Return valid deposit amount
            else:
                print("Please enter a positive number.")
        else:
            print("Please enter a number.")

def get_number_of_lines():
    """
    Prompts the user to enter the number of lines they want to bet on.
    :return: Valid number of lines.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines  # Return valid number of lines
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

def get_bet():
    """
    Prompts the user to enter their bet amount per line.
    :return: Valid bet amount.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount  # Return valid bet amount
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

def spin(balance):
    """
    Handles the slot machine spin and bet deduction.
    (balance) Current balance of the player.
    (return) Net result (win/loss) from the spin.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have sufficient funds to place that bet, your current balance is: ${balance}")
        else:
            break  # Break if the bet is valid

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Generate a spin
    print_slot_machine(slots)  # Display the slot machine spin

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Check for winnings
    print(f"You won ${winnings}.")
    
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines this time.")

    return winnings - total_bet  # Return net result

def main():
    """
    Main function to control the game loop.
    """
    balance = deposit()  # Get initial deposit from player
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")  # Ask player to continue or quit
        if answer.lower() == "q":
            break  # Quit the game loop if 'q' is entered
        balance += spin(balance)  # Update balance with winnings/losses

    print(f"You left with ${balance}")  # Show final balance

# Run the game
main()
