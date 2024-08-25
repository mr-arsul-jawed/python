num = int(input("Enter an integer : "))
def findFact(num):
    fact = num
    for i in range(1,num):fact *= i
    return fact
print("factorial of ",num ,"is : ",findFact(num))