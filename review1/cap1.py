def tipos_de_dados_string():
    texto = "    este é um      pEdAÇo de texto     "
    num_inteiro = 7
    outro_inteiro = 3
    num_quebrado = 9.7
    booleano = True  # ou False

    # print(texto)
    # print('|', texto.strip(), '|', sep='')
    # print('|', texto.rstrip(), '|', sep='')
    # print('|', texto.lstrip(), '|', sep='')
    # print('|', texto, '|', sep='')
    # print('|', texto.strip().title(), '|', sep='')

    curso = '520 PyTHon Fundamentals'
    # print(curso.upper())
    # print(curso.lower())
    # print(curso.capitalize().title().lower().upper())
    # print(curso)
    curso_particionado = curso.partition(' ')
    # print(curso_particionado)
    # print(curso_particionado[0])
    # print(curso_particionado[1])
    # print(curso_particionado[2])
    esq, sep, dir = curso.partition('H')
    # print(esq)
    # print(sep)
    # print(dir)
    esq, sep, dir = curso.rpartition(' ')
    # print(esq)
    # print(sep)
    # print(dir)

    pedacos = curso.split('a')
    # print(pedacos)
    pedacos = curso.rsplit(' ', 1)
    print(pedacos)

def frequencia_caracteres(s):
    frequencias = {}

    for c in s:
        if c in frequencias:
            frequencias[c] += 1

        else:
            frequencias[c] = 1

    return frequencias

def operadores_aritmeticos(x, y):
    print(f"x = {x}, y = {y}")
    print("x + y = {} + {} = {:.2f}".format(x, y, x + y))
    print("x - y = {1} - {0} = {2:.6f}".format(y, x, x - y))
    print("x * y = {vx} * {vy} = {mult:.0f}".format(vx=x, mult=x*y, vy=y))
    print("x / y = %s / %s = %.20f" % (x, y, x / y))
    print()

def operadores_logicos(p, q, r):
    print(dict(p=p, q=q, r=r))
    # operador E (and): verdadeiro quando ambos/todos verdadeiros
    print('and')
    print(p, q, p and q)
    print(p, r, p and r)
    print(p, q, r, p and q and r)

    # operador OU (or): falso quando ambos/todos verdadeiros
    print('or')
    print(p, q, p or q)
    print(p, r, p or r)
    print(p, q, r, p or q or r)
    print(r, r or False)

    print('short circuit')
    resultado = 2 and 3
    print(resultado)
    print(2 or 3)
    print(0 and 3)
    print(0 or 3)
    print(0 and 1/0)

    # operador NÃO (not): nega um booleano
    print('not')
    print(True, not True)
    print(False, not False)

# tipos_de_dados_string()
# print(frequencia_caracteres('GNU/Linux é um sistema Unix'))

# operadores_aritmeticos(2, 3)
# operadores_aritmeticos(7, 4.5)
# operadores_aritmeticos(4.4, 3.14)
# operadores_aritmeticos(10, 0)

operadores_logicos(True, True, False)
