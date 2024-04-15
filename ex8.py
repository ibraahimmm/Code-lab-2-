# Number of rows in the pattern
rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after printing each row
