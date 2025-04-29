secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

n = int(input("Guess What Number I've picked for you: "))

while n != secret_number:
    n = int(input("Guess What Number I've picked for you: "))

print("You Won!")
