hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

total_mins = mins + dura

hour = (hour + total_mins // 60) % 24
#number of hours in the total mins by integer dividing with 60
#Adding it to the given hour for the total hours passed
#Dividing with 24 to find actual clock time
mins = total_mins % 60
#Remainder of the division of total_mins and 60 is minutes within 60
print(hour, ":", mins, sep='')

