# px=1
# py=1
# bx=2
# by=2
p = {
    "x":1,
    "y":1
}
b = {
    "x":2,
    "y":2
}
while True:
    for y in range (4):
        for x in range(4):
            if x==p["x"] and y==p["y"]:
                print("P ",end="")
            elif x== b["x"] and y == b["y"]:
                print("B ", end="")
            elif x==1 and y ==3:
                print("G ",end="")
            else:
                print("- ",end="")
        print()
    move = input("Your move W/A/S/D?").upper()
    next_px = p["x"]
    next_py= p["y"]
    box_bx = b["x"]
    box_by=b["y"]

    dx = 0
    dy = 0
    if move =="D":
        dx = 1
    elif move =="A":
        dx = -1
    elif move == "S":
        dy = 1
    elif move == "W":
        dy = -1

    next_px += dx
    next_py +=dy

    if 0<= next_px < 4 - box_b:
        p["x"] = next_px
    if 0<= next_py < 4:
        p["y"] = next_py
    if next_px==box_bx and next_py==box_by:
        box_bx += dx
        box_by +=dy
    if 0<= box_bx <4:
        b["x"]=box_bx
    if 0<= box_by < 4:
        b["y"]=box_by
        # if b["x"] == 1 and b["y"]==3:
        #     print(winnn)
