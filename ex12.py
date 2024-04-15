import math

# Function to calculate the area of a square
def calculate_square_area():
    side_length = float(input("Enter the length of a side of the square: "))
    area = side_length ** 2
    print("The area of the square is:", area)

# Function to calculate the area of a circle
def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is:", area)

# Function to calculate the area of a triangle
def calculate_triangle_area():
    base = float(input("Enter the length of the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print("The area of the triangle is:", area)

# Display menu and ask for user input
while True:
    print("\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")
    print("4: Exit")
    
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        calculate_square_area()
    elif choice == '2':
        calculate_circle_area()
    elif choice == '3':
        calculate_triangle_area()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
