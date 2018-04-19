# for i in range(10):
#     for j in range(10):
#         if (i+j)%2:
#             print ("0"," ",end="")
#         else:
#             print("1"," ",end="")
#     print()
n=int(input("enter a number:"))
for i in range(n):
    for j in range(n):
        if (i+j)%2:
            print ("0"," ",end="")
        else:
            print("1"," ",end="")
    print()
