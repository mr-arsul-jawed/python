num = int(input("Enter an integer : "))
def isPrime(num):
    for i in range(2, num):
        if num % i == 0:return False
    else:return True   
if isPrime(num):print(num, "is a prime.")
else:print(num, "is not a prime.")