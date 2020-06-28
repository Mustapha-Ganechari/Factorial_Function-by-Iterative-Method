def factorial(number):
    fact = 1
    for i in range(number):
        fact=fact*(i+1)
    return fact

number = int(input("Enter the number : "))
print(factorial(number))
