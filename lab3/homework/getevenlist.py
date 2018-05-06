def get_even_list(a):
    for i in a:
        if i % 2 != 0:
            a.remove(i)
    return a

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")


# lista=[1,2,3,4,5]
# lista.remove(1)
# print(lista)
