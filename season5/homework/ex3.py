prices = { "banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
          }
stock = {"banana": 6,
         "apple": 0,
         "orange":32,
         "pear":15}
for key, value in prices.items():
    mess = ''' {0}
    price: {1}
    stock: {2}'''.format(key, prices[key],stock[key])
    print(mess,end="\n")
print()

total = 0
for key, value in prices.items():
    multi = prices[key] * stock[key]
    total += multi
print("total:", total)
