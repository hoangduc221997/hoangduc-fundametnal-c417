# from random import randint, choice
# define
def calc(x, y,op):
    # x=randint(1,10)
    # y=randint(1,10)
    # op = choice(['+','-','*','/'])
    # lista = [1,2,3,4,5,6,7,8,9,10]
    # listb = [1,2,3,4,5,6,7,8,9,10]
    # listop =['+','-','*','/']
    # error = [-2,-1,0,1,2]
    result = 0
    # op ='+'
    # dis_re = 0
    # x = choice(lista)
    # y = choice(listb)
    # op= choice(listop)
    # er=choice(error)

    if op =='+':
        result= x + y
    elif op=='-':
        result= x - y
    elif op=='*':
        result= x * y
    elif op=='/':
        result = x / y

    return result

print(__name__)
if __name__ =="__main__":
    print('eval.py imported')

# print(result)


# usage/call

# calc(3,7, '*')

# result = calc(1,2,'+')
#
# print(result)
