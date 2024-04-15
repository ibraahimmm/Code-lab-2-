# Prompting user to input the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))

# Checking if the lengths satisfy the triangle inequality
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("The lengths provided can form a triangle.")
else:
    print("The lengths provided cannot form a triangle.")
