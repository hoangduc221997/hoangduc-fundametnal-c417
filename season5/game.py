#text game
#incrative
px=1
py=1
while True:
    for y in range (4):
        for x in range(4):
            if x==px and y==py:
                print("P ",end="")
            elif x==px + 1 and y == py + 1:
                print("B ", end="")
            elif x==1 and y ==3:
                print("G ",end="")
            else:
                print("- ",end="")
        print()
    move = input("Your move W/A/S/D?:" ).upper()
    if move == "S":
        py += 1
    elif move =="W":
        py -=1
    elif move =="A":
        px -=1
    elif move =="D":
        px +=1
        # for y in range (4):
        #     for x in range(4):
        #         if x==px and y==py:
        #             print("P ",end="")
        #         elif x==px + 1 and y == py + 1:
        #             print("B ", end="")
        #         elif x==1 and y ==3:
        #             print("G ",end="")
        #         else:
        #             print("- ",end="")
        #     print()
