n = int(input("enter a number:"))
a = 1
if n == 0:
    print("vo nghiem")
else:
    for i in range(n):
        b = a + (a / (1+i))
print(b)
