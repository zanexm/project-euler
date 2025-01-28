# Project Euler Problem 6
# Zane Mendes
# Created: 20/03/2024
# Last Modified: 20/03/2024
indiv_sq_sum = 0
total = 0


for i in range(1,101):
    indiv_sq_sum += i**2
for i2 in range(1,101):
    total += i2
total = total**2
print(total - indiv_sq_sum)