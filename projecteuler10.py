# Zane Mendes
# Date Created: 27-01-2025
# Last Modified: 27-01-2025
# Project Euler 10 
# https://projecteuler.net/problem=10
# Status: Solved


def check_prime(num, primeList):
    assert type(num) == int
    assert num > 1
    
    for i in primeList:
        if num%i == 0:
            return False
    
    return True

def sum_primes():
    total = 0
    primeList = []
    for i in range(2, 2000000):
        if i%10 in [0, 2, 4, 5, 6, 8] and i > 10:
            continue
        else:
            if check_prime(i, primeList) == True:
                primeList.append(i)
                total += i
                # print(i)

    
    return total

print(sum_primes())