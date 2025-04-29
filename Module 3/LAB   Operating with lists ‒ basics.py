my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

index_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in my_list:
    index_list[i] += 1

print("The Original List: ", my_list)

print("The list with unique elements only:", end=" ")

for i in range(len(index_list)):
    if index_list[i] > 0:
        print(i, end=" ")


