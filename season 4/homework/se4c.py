# m = 1
# for i in range(1,11):
#     for j in range(1,11):
#         print(j*m," ",end="")
#     m+=1
#     print()
m = 1
n= int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j*m," ",end="")
    m+=1
    print()
