contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "outro argumento": "qualquer coisa"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(f"Telefone: {telefone}")

nome = contatos["giovanna@gmail.com"]["nome"]  # "Giovanna"
print(f"Nome: {nome}")

outro_argumento = contatos["melaine@gmail.com"]["outro argumento"]  # "qualquer coisa"
print(f"Outro argumento: {outro_argumento}")