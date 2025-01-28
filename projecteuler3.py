# Project Euler Problem 3
# Zane Mendes
# Created: 19/03/2024
# Last Modified: 19/03/2024
def prime(int):
    for i1 in range(2,int):
        if int%i1 == 0:
            if i1 != int:
                return False
    return True

number = 600851475143
highest_prime = 0

for i in range(2,number):
    if number%i == 0:
        if prime(i) == True:
            highest_prime = i
            print(i, "is prime")


print("Highest Prime:", highest_prime)
    

