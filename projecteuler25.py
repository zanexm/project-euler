# Zane Mendes
# Date Created: 21-01-2025
# Last Modified: 27-01-2025
# Project Euler 25 
# https://projecteuler.net/problem=25
# Status: Solved


import math
def fib(fib1, fib2):
    new_fib = fib1 + fib2
    fib1, fib2 = fib2, new_fib
    return fib1, fib2


fib1 = 0
fib2 = 1
counter = 1

while True:
    fib1, fib2 = fib(fib1, fib2)
    counter += 1
    if math.ceil(math.log10(fib2)) == 1000:
        print(counter)
        print(fib2)
        break