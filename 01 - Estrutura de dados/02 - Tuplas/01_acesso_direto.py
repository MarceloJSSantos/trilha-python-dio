frutas = ("maçã", "laranja", "uva", "pera",)

print(frutas[0])  # maçã
print(frutas[2])  # uva


tup = (1,2,3)
print(tup)  # (1, 2, 3)

tup = tup + (4,5,6)
print(tup)  # (1, 2, 3, 4, 5, 6)

tup[0] = 10  # TypeError: 'tuple' object does not support item assignment