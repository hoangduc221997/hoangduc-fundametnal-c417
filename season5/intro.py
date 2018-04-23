# person = ["Quan", 22,"Single","Hanoi", 4, 20]
# print(person)

#descriptive
#dictionary

# person = {}
# print(person)
# Huu Nghia, Hiep,Huy,CLln,Lan,Duc Anh,Vietson,Ha Anh,Minh Anh,Kiet
person ={
    "name":"Quan",
    "age":40,       #key value
}
# print(person)
# print(person["name"])
# person["age"]=22
# print(person)
#
# if "home" in person: #list, str
#     print(person["home"])
# else:
#     print("'home' is not in person")



#CREATE
# person["home"]="Hanoi"
# print(person)
#
#
# del person["age"]
print(*person.values())
print(*person.keys())

for key, value in person.items():
    print(key, ":", value)
