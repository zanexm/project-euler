def prime(int):
    for i1 in range(2,int):
        if int%i1 == 0:
            if i1 != int:
                return False
    return True

list_of_primes = []
i = 2

while len(list_of_primes) < 10001:
    if prime(i) == True:
        list_of_primes.append(i)
    i += 1
print(list_of_primes[10000])