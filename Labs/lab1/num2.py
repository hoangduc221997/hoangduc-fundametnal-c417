nums = [3,4,-99,78,4,-99,3]
x = int(input("Enter a number: "))

for num in nums:
    if num == x:
        print("found")
        break
else:
    print("Not found")
