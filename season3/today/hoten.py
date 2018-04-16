# the 1 cua list
# # names = []
# # print(names)
# # print(type(names)
# #CRUD: creat , read, update, delete
#
# the 2 cua list
# # names =["Canh"]
# # print(names)
#
# 3.
names = ["Canh", "Hieu", "Duc Anh","Dap San","ZXC"]
# print(names)
# Create
# names.append("nguyen")
# print(names)
#
# new_name = "Don"
# names.append("Cac")
# print(names)
# read
# print(names[0])

# names[0] = "Canh cc"
# print (names[0])

# print(len(names)) # len = lenght
#
# for i in range(len(names)):
#     print(names[i])


# #foreach
# n = len(names)
# for name in names:
#     print("n.", name)

no = 1
for n in names:
    # print(no,". ", n,sep="")
    #string format
    message = "{0}. {1}.".format(no,n)
    no += 1
    print(message)
