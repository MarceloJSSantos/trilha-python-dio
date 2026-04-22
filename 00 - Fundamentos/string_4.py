nome = "Guilherme"
NR_CARACTERES = 100

print(str(".").center(NR_CARACTERES,"."))
mensagem = f'''
   Olá meu nome é {nome},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
'''

print(mensagem)

print(str(".").center(NR_CARACTERES,"."))
print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

        Obrigado por usar nosso sistema!!!!
    """
    )