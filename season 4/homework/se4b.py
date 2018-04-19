# number = [1,0]
# for i in range(10):
#     for j in number:
#         print(j,end="")
# print()

n = int(input("Enter a numer:"))
for i in range(n):
    if i % 2:
        print("0"," ",end="")
    else:
        print("1"," ",end="")
print()
