lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

lista_2 = list("marcelo JS Santos")
print(f"lista_2: {lista_2}")  # ['m', 'a', 'r', 'c', 'e', 'l', 'o', ' ', 'J', 'S', ' ', 'S', 'a', 'n', 't', 'o', 's']

print(f"Só Marcelo: {lista_2[0:7]}")  # ['m', 'a', 'r', 'c', 'e', 'l', 'o']
print(f"Só Santos: {lista_2[11:]}")  # ['S', 'a', 'n', 't', 'o', 's']