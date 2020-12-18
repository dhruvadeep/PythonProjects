# getting the factorial of a number

number = int(input("Enter a number: "))
total = 1

for i in range(1, number+1):
    total *= i

print("Answer is: ", total)
