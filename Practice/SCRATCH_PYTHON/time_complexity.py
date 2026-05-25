#How many times loop runs?

#Single loop → linear
#Nested loop → square growth

#for i in range(n): so the time complexity is O(n) means n times loop runs.


# Nested loops Time complexity
n =  10
for i in range(n):
    for j in range(n):
        print(i, j)


# Runs : n*n = n^2 times
#Complexity: O(n^2) - O(n²)


