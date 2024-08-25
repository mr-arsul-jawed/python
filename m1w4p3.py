userInput = list((input("Enter num list :").split()))
numList = []
for x in userInput: numList.append(int(x))
def double(x) : return x * 2
result = map(double, numList)
print(list(result))