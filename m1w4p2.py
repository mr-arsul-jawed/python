userInput = list(input("Enter num list :").split())
numList = []
for num in userInput: numList.append(int(num))
def isEvent(x): return x % 2 == 0
numIterator = filter(isEvent,numList)
print(list(numIterator))