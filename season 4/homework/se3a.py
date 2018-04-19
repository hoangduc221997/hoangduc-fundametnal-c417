
print("WORD_JUMPLE")
from random import choice
text ="comfortable"
a = list(text)
for i in range(len(text)):
    b = choice(a)
    print(b, end=" ")
    a.remove(b)
print()

loop = True
while loop:
    n=input("Your answer:")
    if n != text:
        print(":(")
    else:
        print("Hura")
        loop = False
