num = int(input("Enter count of natural number : "))
sum = num ** 2
for i in range(1,num):sum += i ** 2
print("Sum of squares of first ",num ,"natural numbers : ",sum)