# Looping from 1 to 100
for num in range(1, 101):
    # Checking for multiples of both three and five
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Checking for multiples of three
    elif num % 3 == 0:
        print("Fizz")
    # Checking for multiples of five
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
