num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
double = lambda num1 : num1 * 2
sum = lambda num1, num2 : num1 + num2
print("Double :", double(num1), double(num2))

print("Sum :", sum(num1,num2))