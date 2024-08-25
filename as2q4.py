num = int(input("Enter an integer : "))
def isArmstrong(num):
    temp1 = temp2 = num
    sum = 0
    count = 0
    while temp1 != 0:
        count += 1
        # temp1 //= 10
        temp1 = int(temp1 / 10)
    while temp2 != 0:
        rem = temp2 % 10
        sum += rem ** count
        # temp2 //= 10
        temp2 = int(temp2 / 10)
    if num == sum:return True
    else:return False
if isArmstrong(num):print(num ,"is armstrong.")
else:print(num ,"is not armstrong.")