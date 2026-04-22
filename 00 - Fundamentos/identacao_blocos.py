saldo = 0

def sacar(valor):
    global saldo

    if saldo >= valor:
        saldo -= valor
        print(f"valor sacado! Saldo: {saldo}")
        print("retire o seu dinheiro na boca do caixa.")
    else:
        print(f"valor não sacado! Saldo: {saldo}")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):
    global saldo
    saldo += valor
    print(f"valor depositado! Saldo: {saldo}")

depositar(1000)
sacar(800)
depositar(10000)
