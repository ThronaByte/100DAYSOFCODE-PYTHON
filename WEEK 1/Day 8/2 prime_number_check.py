# Prime number checker
n = int(input("Enter number: "))
# method 1
def prime_checker(number):
    is_prime = True
    for i in range(2, number -1):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it's a prime")
    else:
        print("it's not a prime")
prime_checker(number=n)