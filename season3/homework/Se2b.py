sheepsize = [5,7,300,90,24,50,75]
print("Hello, I'm D and here is my flock", sheepsize)
for i in range(3):
    print("month",i+1,":")
    for j in range(len(sheepsize)):
        sheepsize[j] +=50
    print("One month has passes now here is my flock", sheepsize)
    print("Now my biggest sheep has size",max(sheepsize),"let's shear it")
    sheepsize[sheepsize.index(max(sheepsize))] = 8
    print ("After shearing it, here is my flock", sheepsize)


s = sum(sheepsize)
print("My flock has size in total:", s)
money = s * 2
print("I would get all", money, "$ hehe")
