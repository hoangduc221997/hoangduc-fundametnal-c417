x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

op = input("Operation(+,-,*,/): ")
result  = 0
if op =='+':
    result= x+y
elif op=="-":
    result = x-y
elif op=="*":
    result=x*y
elif op=="/":
    result=x/y
else:
    print("Wrong")
print("* "*10)
print("{0}{1}{2}={3}".format(x,op,y,result))
print("* "*10)
