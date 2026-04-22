while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        print(f"Número 10: Finalizado")
        break

    if numero % 2 == 0:
        print(f"Número par: {numero}")
        continue

    print(f"Número ímpar: {numero}")


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")
