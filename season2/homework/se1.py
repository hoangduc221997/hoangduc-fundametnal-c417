a = float(input("your weight:")) #don vi (m)
b = float(input("input your height:")) #don vi (kg)
c = a /(b*b)
print(c)
if c<16:
    print("severely underweight")
elif 16 <= c <18.5:
    print("underweight")
elif 18.5 <= c < 25:
    print("normal")
elif 25 <= c < 30:
    print("overweight")
else:
    print("obese")
