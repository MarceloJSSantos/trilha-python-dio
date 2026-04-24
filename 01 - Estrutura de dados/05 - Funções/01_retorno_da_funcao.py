def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def retorna_none():
    print("Essa função não retorna nada")
    
numeros = [10, 20, 34]
numero = 10
print(f"Calcula o Total de {numeros}: {calcular_total(numeros)}")  # 64
print(f"Retorna o Antecessor e Sucessor de {numero}: {retorna_antecessor_e_sucessor(numero)[0]} e {retorna_antecessor_e_sucessor(numero)[1]}")  # (9, 11)
print(f"Retorna None: {retorna_none()}")  # None
