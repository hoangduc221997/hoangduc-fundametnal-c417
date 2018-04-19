
from getpass import getpass
loop = True
wrong_count = 0
while loop:
    a = input("Username:")
    b = getpass("Password:")
    # if a == "ducdz":
    #     if b != "FuckEr":
    #         print("wrong password")
    #     else:
    #         print("Welcome")
    # else:
    #     print("Wrong bitch")
    if a != 'ducdz':
        print("Wrong Bitch")
        wrong_count += 1
    elif b != 'FuckEr':
        print("Wrong pass")
        wrong_count += 1
    else:
        print("Welcome to the world")
        loop = False
    if wrong_count >3:
        loop = False
