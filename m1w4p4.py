import functools

userInput = list((input("Enter num list :").split()))
numList = []
for x in userInput: numList.append(int(x))
def double(x,y) : return x + y
result = functools.reduce(double, numList)
print(result)