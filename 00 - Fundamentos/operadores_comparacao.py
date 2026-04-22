saldo = 200
saque = 300

operador = " == "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Igual: {comparacao} -> {eval(comparacao)}")
operador = " != "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Diferente: {comparacao} -> {eval(comparacao)}")
operador = " > "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Maior que: {comparacao} -> {eval(comparacao)}")
operador = " >= "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Maior/Igual que: {comparacao} -> {eval(comparacao)}")
operador = " < "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Menor que: {comparacao} -> {eval(comparacao)}")
operador = " <= "
comparacao = "" + str(saldo) + operador + str(saque)
print(f"Menor/Igual que: {comparacao} -> {eval(comparacao)}")
