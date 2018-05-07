import random
from random import choice
import eval

def generate_quiz():
    x = random.randint(1,10)
    y=random.randint(1,10)
    op=choice(["+","-","*","/"])
    # Hint: Return [x, y, op, result]
    result=eval.calc(x,y,op)
    error=choice([-1,0,1])
    dis_result= result + error

    return [x, y, op, dis_result]


def check_answer(x, y, op, result, user_choice):
    # user_choice: True, False
    if eval.calc(x,y,op) == result:
        if user_choice == True:
            return True
        elif user_choice == False:
            return False
    if eval.calc(x,y,op)!= result:
        if user_choice == True:
            return False
        if user_choice == False:
            return True
