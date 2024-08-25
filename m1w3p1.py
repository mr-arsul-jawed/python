def sumTheNumbers(num1, num2) :
    print("Sum =", num1 + num2)

def multiplyTheNumbers(num1, num2) :
    print("Product = ", num1 * num2)

def subtractTheNumbers(num1, num2) :
    print("Difference = ", num1 - num2)

def  divideTheNumbers(num1, num2): 
    print("Quotient = ", num1/num2)

while True :
    choice = input("TO PERFORM ADDITION type : add \nTO PERFORM SUBSTRACTION  type: subtract \nTO PERFORM MULTIPLICATION TYPE : multiply \nTO PERFORM DIVISION type : divide \nTO CLOSE the program type : close :: ")
    if choice == "add" :
        num1 = int(input("Enter the augend:"))
        num2 = int(input("Enter the addend:"))
        sumTheNumbers(num1,num2)
    elif choice == "subtract" :
        num1 = int(input("Enter the subtrahend:"))
        num2 = int(input("Enter the minued:"))
        subtractTheNumbers(num1,num2)
    elif choice == "multiply" :
        num1 = int(input("Enter the multiplier:"))
        num2 = int(input("Enter the multiplicand:"))
        multiplyTheNumbers(num1,num2)
    elif choice == "divide" :
        num1 = int(input("Enter the dividend:"))
        num2 = int(input("Enter the divisor:"))
        divideTheNumbers(num1,num2)
    elif choice == "close" :
        break
    else : print("Try again.")