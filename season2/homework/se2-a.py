n = int(input("enter a number:"))
a = 1
if n == 0:
    a = 0
else:
    for i in range(n):
        a = a * (i+1)
print(a)
