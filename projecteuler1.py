# Project Euler Problem 1
# Zane Mendes
# Created: 19/03/2024
# Last Modified: 19/03/2024

# Sum of multiples of 3 and 5
x = 0
y = 0
z = 0
sum = 0

while 3*x < 1000:
    sum += 3*x
    x += 1
while 5*y < 1000:
    sum += 5*y
    y += 1
while 15*z < 1000:
    sum -= 15*z
    z += 1
print(sum)