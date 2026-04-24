def salvar_carro(formato_argumento, marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"{formato_argumento} - Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Posicional", "Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(formato_argumento="Nomeado", marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"formato_argumento": "Nomeado por Dicionário", "marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
