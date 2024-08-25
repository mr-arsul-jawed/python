n = int(input("Enter n :"))
mid = n
for i in range(n):
    for j in range(n + 1):
        if(j <= i):
            print(end=" ")
        else :
            for k in range(mid):
                print("*",end="")
            mid = mid - 1
            break
    print()