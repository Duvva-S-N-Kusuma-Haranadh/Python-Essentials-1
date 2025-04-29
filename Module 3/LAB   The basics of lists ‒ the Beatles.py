beetles = []

beetles.append("John Lennon")
beetles.append("Paul McCartney")
beetles.append("George Harrison")

print("Appending Stu Sutcliffe and Pete Best: ")

print(beetles)

for i in range(2):
    beetles.append(input("Enter the name: "))

print(beetles)

print("Deleting Stu Sutcliffe and Pete Best from the list: ")
del beetles[3]
del beetles[3]

print(beetles)

print("Inserting Ringo Starr at first position: ")

beetles.insert(0, "Ringo Starr")

print(beetles)

# testing list legth
print("The Fab", len(beetles))

