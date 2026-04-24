lista = [1, "Python", [40, 30, 20]]

print(f"lista original: {lista}")  # [1, "Python", [40, 30, 20]]

lista_2 = list(lista.copy()[0:2])
print(f"lista_2: {lista_2}")  # [1, "Python", [40, 30, 20]]

print(f"Ids das listas: lita={id(lista)}, lista_2={id(lista_2)}")  # Ids das listas: 140432678901568, 140432678901632
