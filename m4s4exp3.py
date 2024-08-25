alphabets = ["A","B","C", "D", "E"]
n = len(alphabets)
mid = n * 2 - 1
for i in range(n):
    for j in range(n * 2):
        if(j <= i):
            print(end=" ")
        else :
            for k in range(mid):
                print(alphabets[n - i - 1],end="")
            mid = mid - 2
            break
    print()