produto_1 = 20
produto_2 = 10

print(f"Adição: {produto_1} + {produto_2} = {produto_1 + produto_2}")
print(f"Subtração: {produto_1} - {produto_2} = {produto_1 - produto_2}")
print(f"Divisão: {produto_1} / {produto_2} = {produto_1 / produto_2}")
#Divisão inteira
print(f"Divisão inteira: {produto_1} // {produto_2} = {produto_1 // produto_2}")
print(f"Multiplicação: {produto_1} * {produto_2} = {produto_1 * produto_2}")
print(f"Resto da Divisão: {produto_1+1} % {produto_2} = {(produto_1+1) % produto_2}")
print(f"Exponenciação: {produto_1} ** {produto_2//5} = {produto_1 ** (produto_2//5)}")

#Precedência
#Parenteses
#exponeciação
#multiplicação e divisão
#adição e subtração
x = "(10 + 5) * 4"
y = "(10 / 2) + 25 * ((2 - 2) ** 2)"
print(f"Precedência (expressão X): {x} = {eval(x)}")
print(f"Precedência (expressão Y): {y} = {eval(y)}")
