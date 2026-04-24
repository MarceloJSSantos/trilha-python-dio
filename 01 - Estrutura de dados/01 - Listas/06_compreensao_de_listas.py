# Filtrar lista
print("Filtrar lista".center(30, "."))
numeros = [1, 30, 21, 2, 9, 65, 34]
print(f"numeros: {numeros}")

pares = [numero for numero in numeros if numero % 2 == 0]
print(f"pares: {pares}")

impares = [numero for numero in numeros if numero % 2 != 0]
print(f"impares: {impares}")

print()
# Modificar valores
print("Modificar valores".center(30, "."))
numeros = [1, 30, 21, 2, 9, 65, 34]
print(f"numeros: {numeros}")
quadrado = [numero**2 for numero in numeros]
print(f"quadrado de 'numeros': {quadrado}")
