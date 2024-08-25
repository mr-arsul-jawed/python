str = input("Enter a string :")
len = len(str)
for i in range(len // 2) : 
    if str[i] != str[len - i - 1] : 
        print(str, "is not a palindrome")
        break
else : print(str, "is a palindrome")