list = [5, 6, 7, 10, 12, 44,100]
n = list
x = int(input("Enter a number:"))
#in
if x in list:
    print("yes")
else:
    print("no")
#occurences => count()

c = list.count(x)
print(c)
