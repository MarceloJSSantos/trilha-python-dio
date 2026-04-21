nome = "Guilherme"
idade = 28

#as variáveis nome e idade foram alteradaa
nome, idade = "Giovanna", 27

print(nome, idade)
print(f'A {nome} tem {idade} anos de idade.')

limite_saque_diario = 1000
print(f'O seu limite diário de saque é {limite_saque_diario}.')

#A constante não deve ser alterada
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]
print(BRAZILIAN_STATES)

#Mas em Python as constantes podem ser alteradas, MAS NÂO SÃO UMA BOA PRÁTICA
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS", "BA", "MG"]
print(BRAZILIAN_STATES)
