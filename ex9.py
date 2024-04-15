# Create an int list with 10 values
int_list = [7, 3, 12, 5, 9, 2, 8, 4, 6, 10]

# Output the list using a for loop
print("Original list:")
for num in int_list:
    print(num, end=" ")
print()

# Output the highest and lowest value
print("Highest value:", max(int_list))
print("Lowest value:", min(int_list))

# Sort the elements in ascending order
int_list.sort()
print("Sorted list in ascending order:", int_list)

# Sort the elements in descending order
int_list.sort(reverse=True)
print("Sorted list in descending order:", int_list)

# Append two elements
int_list.append(11)
int_list.append(1)

# Print the list after appending
print("List after appending two elements:", int_list)
