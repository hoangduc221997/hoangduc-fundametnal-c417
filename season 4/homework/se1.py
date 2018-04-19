number = [1,6,8,1,2,1,5,6]
n = int(input("Enter number:"))
count = 0
for i in number:
    if i ==n:
        count+=1
print("{0} appear {1} times in my list!".format(n,count))
