
print("WORD_JUMPLE")
from random import choice
from random import randrange
word_list = ["meticulous","champion","hexagon"]
loop = len(word_list)
c = 0
while loop > c:
    text = choice(word_list)
    word=list(text)

    w =""
    while word:
            a=randrange(len(word))
            w += word[a]
            word=word[:a] + word[(a+1):]
    print(*list(w), sep="  ")
    n = input("Your answer:").lower()
    if n != text:
        print(":(")
    else:
        print("Hura")
        c += 1
