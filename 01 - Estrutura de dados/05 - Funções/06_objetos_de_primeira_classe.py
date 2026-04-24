def somar(a, b):
    return '+', a + b

def subtrair(a, b):
    return '-', a - b

def multiplicar(a, b):
    return '*', a * b

def dividir(a, b):
    if b == 0:
        return '/', 'Erro: Divisão por zero'
    return '/', a / b

def potencia(a, b):
    return '**', a ** b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} {resultado[0]} {b} = {resultado[1]}")

exibir_resultado(10, 3, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado(10, 3, subtrair)  # O resultado da operação 10 - 10 = 0
exibir_resultado(10, 3, multiplicar)  # O resultado da operação 10 * 10 = 100
exibir_resultado(10, 2, dividir)  # O resultado da operação 10 / 10 = 1.0
exibir_resultado(10, 3, potencia)  # O resultado da operação 10 ** 10 = 10000000000    