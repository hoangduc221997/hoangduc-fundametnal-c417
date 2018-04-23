dict = {
    "any":"Anh nguoi yeu",
    "Ced":"Choi em di",
    "420":"hut can khong",
    "dm":"dau ma",
    "dkm":"Dinh cong menh"
}
print(*dict)
while True:
    m =input("Your code? ")
    if m in dict:
        print("Translation:",dict[m])
    else:
        print(m, " not exist","Do u wanna add? ",end="")
        n= input("").upper()
        if n == "Y":
            Trans=input("Your Translation:")
            dict[m]=Trans
            print(*dict)
        elif n == "N":
            print("Thanks")
        else:
            print("Sai cu phap, du me may")
