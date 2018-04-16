print("Hello i'm Mr.D and these are my fucking sheet size :D")
sheepsize = [5,7,300,90,24,50,75]
print(sheepsize)

maxsheep =max(sheepsize)
print("Now is my biggest sheep has size", maxsheep, "let's shear it")

sheepsize[2]=8
print("After sheering, here is my flock", sheepsize)

for i in range(len(sheepsize)):
    sheepsize[i] += 50
print ("One month has passed, now here is my flock", sheepsize)
