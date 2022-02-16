def geracoes(ano):
    if ano <= 1964:
        return 'Baby Boomer'

    elif ano <= 1979:
        return 'Geração X'

    elif ano <= 1994:
        return 'Geração Y'

    else:
        return 'Geração Z'


def geracoes_dict(ano):
    gs = {1964: 'Baby Boomer', 1979: 'Geração X', 1994: 'Geração Y'}

    for (geracao_ano, geracao_nome) in gs.items():
        if ano <= geracao_ano:
            return geracao_nome
    #     else:
    #         return 'Geração Z'

    return 'Geração Z'

ano_nascimento = 2000 #int(input("Digite o seu ano de nascimento: "))
print(f"Você faz parte da geração {geracoes_dict(ano_nascimento)}")
