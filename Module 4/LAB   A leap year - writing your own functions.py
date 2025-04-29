# The code uses two lists ‒ one with the test data, and the other containing the expected results. The code will tell you if any of your results are invalid.

def is_year_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 !=0:
        return True
    return False

test_data = [1900, 2100, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
