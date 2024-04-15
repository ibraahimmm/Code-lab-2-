# Function to calculate the product of values in a list
def calculate_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Main program
if __name__ == "__main__":
    # Example list
    numbers = [2, 3, 4, 5, 6]
    
    # Calculate the product of values in the list
    result = calculate_product(numbers)
    
    # Output the result
    print("The product of the values in the list is:", result)
