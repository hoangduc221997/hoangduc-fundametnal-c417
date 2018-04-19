from random import *
n = randint (0,100)
a = 0
print("Guess my number, fucker")
loop = True
while loop:
    m = int(input("Enter number:"))
    if n == m:
        print("Bingo")
        loop = False
    elif n < m:
        print("too large")
        a += 1
    elif n > m:
        print("too small")
        a += 1
    if a > 8:
        print("Game over, Fucker")
        loop = False
