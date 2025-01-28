# Project Euler Problem 5
# Zane Mendes
# Created: 20/03/2024
# Last Modified: 20/03/2024

passed = False
i = 1
while passed == False:
    if i%11 == 0 and i%12 == 0 and i%13 == 0 and i%14 == 0 and i%15 == 0 and i%16 == 0 and i%17 == 0 and i%18 == 0 and i%19 == 0 and i%20 == 0:
        passed = True
        print(i)
    else:
        i += 1
# takes a minute or two to solve it so be patient
        