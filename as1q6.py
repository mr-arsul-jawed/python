num = int(input("Enter an integer : "))
count = 0
for i in range(2, num):
    if num % i == 0 :
        print(num ,"is not prime.")
        break
else :
    print(num ,"is prime.")