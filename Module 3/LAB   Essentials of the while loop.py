blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#

count = 1
height = 0

while blocks > count:
    height = height + 1
    count = count + height + 1

print("The height of the pyramid:", height)

