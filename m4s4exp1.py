alphabets = ["A","B","C", "D", "E"]
n = len(alphabets)
mid = n - 1
for i in range(n):
    for j in range(n):
        if(j == mid):
            for k in range(i + 1):
                print(" ",alphabets[k],end=" ")
            mid = mid - 1
            break
        else :
            print(end="  ")
    print()