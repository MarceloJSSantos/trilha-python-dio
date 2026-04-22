nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435
NR_CARACTERES = 100

print(str(".").center(NR_CARACTERES,"."))
print("Nome: %s Idade: %d" % (nome, idade))

print(str(".").center(NR_CARACTERES,"."))
print("Nome: {} Idade: {}".format(nome, idade))

print(str(".").center(NR_CARACTERES,"."))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1} {1} {1}".format(idade, nome))

print(str(".").center(NR_CARACTERES,"."))
dados = {"nome": "Guilherme", "idade": 28}
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(str(".").center(NR_CARACTERES,"."))
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.3f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:15.6f}")
print(str(".").center(NR_CARACTERES,"."))