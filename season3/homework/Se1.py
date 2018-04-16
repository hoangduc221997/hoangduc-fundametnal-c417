list = ["T-shirt"," Sweeter"]
while True:
    print("> Weclome to our shop <")
    i = input("what do you want (C, R, U, D)? ")
    if i == "R":
        print("out items:", end="")
        print(*list, sep= ", ")
    if i == "C":
        new =input("New items:")
        list.append(new)
        print(*list, sep= ", ")
    if i == "U":
        position = int(input("Update position? "))
        items = input("new items ?")
        list[posititon - 1] = itmes
        print(*list, sep= ", ")
    if i == "D":
        delete = int(input("Delete position:"))
        del list[delete -1]
        print(*list, sep= ", ")
    else:
        print("Invalid Function")
Print("Get out Ass hole!")
