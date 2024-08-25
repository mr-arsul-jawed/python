num = int(input("Enter an integer : "))
fact = num
for i in range(1,num):
    fact *= i
print("factorial of ",num ,"is : ",fact)