inventory = {"apples":430,
             "bananas":312,
             "oranges":525,
             "pears": 217}
# # # # # print(inventory)
# # # # # del inventory["pears"]
# # # # # # print(inventory)
# # # # # inventory["prears"] = 0
# # # # # inventory["bananas"] +=200
# # # # # print(len(inventory))
# # # # # for k in inventory.keys():
# # # # #     print("Got key", k ,"which map to value",inventory[k])
# # # # # ks = list(inventory.keys())
# # # # # print(ks)
# # # #
for k , v in inventory.items():
    print(k)
    print(inventory[k])
# # #
# # #
# # # opposites = {"up":"down",
# # #              "right":"wrong",
# # #              "yes":"no"}
# # # alias = opposites
# # # copy = opposites.copy()
# # # alias["right"] = "left"
# # # print(opposites["right"])
# # # copy["right"]="fuck"
# # # print(opposites["right"])
# #
# #
# # alreadyknown= {0:0,1:1}
# # n=int(input("Number"))
# # def fib(n):
# #     if n not in alreadyknown:
# #         new_value = fib(n-1) + fib(n-2)
# #         alreadyknow[n] = new_value
# #     return alreadyknown[n]
# #     fib(100)
#
#
# letter_counts ={}
# for letter in "Mississippi":
#     letter_counts[letter]=letter_counts.get(letter, 0) + 1
# print(letter_counts)
