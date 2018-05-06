from random import choice

# x=randint(1,10)
# y=radint(1,10)
# op = choice
lista = [1,2,3,4,5,6,7,8,9,10]
listb = [1,2,3,4,5,6,7,8,9,10]
listop =['+','-','*','/']
er = choice([-2,-1,0,1,2])
result = 0
dis_re = 0
x = choice(lista)
y = choice(listb)
op= choice(listop)
# er=choice(error)

if op =='+':
    result= x + y
    dis_re= result + er
elif op=='-':
    result= x - y
    dis_re= result + er
elif op=='*':
    result= x * y
    dis_re= result + er
elif op=='/':
    result = x / y
    dis_re= result + er

print("* " * 15)
print("{0} {1} {2} = {3}".format(x,op,y,dis_re))
print("* " * 15)

ans= input("Y/N: ").lower()
if er == 0 and ans == 'y':
    print('Yay')
elif er != 0 and ans =='n':
    print('Yay')
elif er == 0 and ans == 'n':
    print("Wrong Fucker")
elif er != 0 and ans =='y':
    print('Wrong Fucker')
