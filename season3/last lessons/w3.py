n =int(input("enter fucking row:"))
m =int(input("enter fucking column:"))
for i in range(n):
    for j in range(m):
        if (i + j) % 2 !=0:
            print(" 0",end="")
        else:
            print(" *", end="")
    print()
