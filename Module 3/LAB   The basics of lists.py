hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)

n = int(input("Enter any number to replace the middle number of the list: "))

hat_list[len(hat_list)//2] = n

del hat_list[len(hat_list) - 1]

print("List length: ", len(hat_list))

print(hat_list)


