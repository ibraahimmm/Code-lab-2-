# Prompting user to input two integer numbers
num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))

# Performing arithmetic calculations
sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
remainder_result = num1 % num2

# Outputting the results to the console
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {diff_result}")
print(f"Product: {num1} x {num2} = {product_result}")
print(f"Quotient: {num1} / {num2} = {quotient_result}")
print(f"Remainder: {num1} % {num2} = {remainder_result}")
