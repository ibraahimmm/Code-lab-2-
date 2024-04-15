count = 0  # Initialize a counter to keep track of loop iterations

# While loop to keep looping as long as user enters 'Y'
while True:
    # Asking the user if they would like to continue
    choice = input("Would you like to continue? (Y/N): ")

    # Incrementing the counter
    count += 1

    # Checking if the user wants to continue or not
    if choice.upper() != 'Y':
        break  # Exit the loop if the user enters any character other than 'Y'

# Outputting the number of times the loop is executed
print(f"The loop executed {count} times.")
