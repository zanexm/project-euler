# Project Euler Problem 2
# Zane Mendes
# Created: 19/03/2024
# Last Modified: 19/03/2024

fib_1 = 0
fib_2 = 1
fib_placeholder = 0
total_even = 0

while fib_1 + fib_2 < 4000000:
    fib_placeholder = fib_1
    fib_1 = fib_2
    fib_2 = fib_1 + fib_placeholder
    if fib_2%2 == 0:
        total_even += fib_2
        # print(fib_1)
print("Total: ", total_even)

