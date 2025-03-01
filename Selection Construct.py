# Problem 1:
    
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
# message to the user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
    
# 1. If the number is a multiple of 4, print out a different message.

# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by
# (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate
# message.

# Ask the user for a number
num = int(input("Enter a number: "))

# Check if the number is even or odd
if num % 2 == 0:
    if num % 4 == 0:
        print(f"{num} is even and also a multiple of 4.")
    else:
        print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Extra: Ask for another number to divide by
check = int(input("Enter a number to divide by: "))

# Check divisibility
if num % check == 0:
    print(f"{num} is evenly divisible by {check}.")
else:
    print(f"{num} is not evenly divisible by {check}.")
