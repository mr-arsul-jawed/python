num = int(input("Enter count of fibonacci series : "))
fib = [0] if num == 0 or num == 1 else [0,1]
for i in range(2,num):fib.append(fib[i - 1] + fib[i - 2])
print(num ,"fibonacci series :",fib)