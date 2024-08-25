num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
min = num1 if num1 < num2 else num2
prime = list()
for i in range(2,(min // 2) + 1):
    count = 0
    for j in range(2,(i // 2) + 1):
        if i % j == 0:
            count += 1
            break
    if count == 0:prime.append(i)
fact1 = list()
fact2 = list()
primeIter1 = iter(prime)
current_prime = next(primeIter1)
while num1 >= 2:
    if num1 % current_prime == 0:
        num1 //= current_prime
        fact1.append(current_prime)
    else:
        if current_prime == prime[-1]:
            break
        else:
            current_prime = next(primeIter1)
primeIter2 = iter(prime)
current_prime = next(primeIter2)
while num2 >= 2:
    if num2 % current_prime == 0:
        num2 //= current_prime
        fact2.append(current_prime)
    else:
        if current_prime == prime[-1]:
            break
        else:
            current_prime = next(primeIter2)
min = fact1.copy() if len(fact1) < len(fact2) else fact2.copy()
gcd = 1
for fact in min:
    if fact in fact1 and fact in fact2:
        fact1.remove(fact)
        fact2.remove(fact)
        gcd *= fact
print("GCD = ",gcd)