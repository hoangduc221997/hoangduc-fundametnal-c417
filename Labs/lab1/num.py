nums = [3, 4, -99, 78, 4 ,-99, 3]
x = int(input("Enter an integer:"))
# must not use count() or in or index()
found = False
for num in nums:
    if num ==x:
        print("Found!!!")
        found = True
        break
# if found:
#     print("Found")
# else:
#     print("not found")




#Linear search
