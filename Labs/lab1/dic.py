person = {
    "name":"Quan",
    "age":22,
    "gender":"undefined",
    "address":"Hanoi",
    "login_count": 7
}
#if "name" in person:
#if "name" in person.keys():
print(person.keys()) #get all keys
print(person.values())
# if "Quan" in person.values():
#     print("Yeah")
print(person["name"])

values = list(person.values())
