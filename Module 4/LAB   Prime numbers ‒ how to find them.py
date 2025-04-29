def is_prime(num):
    flag = True
    for i in range(2, num // 2):
        if num % i == 0:
            flag = False
    
    return flag

range_ = int(input("Enter the range: "))
for i in range(1, range_):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
