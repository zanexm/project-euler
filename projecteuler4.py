# Project Euler Problem 4
# Zane Mendes
# Created: 20/03/2024
# Last Modified: 20/03/2024
highest_palendrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if str(i*j) == str(i*j)[::-1]:
            palendrome = i*j
            if highest_palendrome < palendrome:
                highest_palendrome = palendrome
                print(highest_palendrome)
            

         