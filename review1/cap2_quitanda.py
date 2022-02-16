quitanda_lista = 'Banana:3.50 Melancia:7.50 Morango:5.00 Laranja:2.75'.split()
quitanda = {}

for fruta in quitanda_lista:
    fruta, preco = fruta.split(':')
    quitanda[fruta] = float(preco)

cesta = {}
for fruta in quitanda:
    cesta[fruta] = 0

def menu_principal():
    opcoes = {'1': 'Ver cesta', '2': 'Adicionar fruta',
              '3': 'Checkout', '4': 'Sair'}

    for (op, desc) in opcoes.items():
        print("{numero} - {texto}".format(numero=op, texto=desc))

    escolha = input("Digite a opção desejada: ")

    return opcoes.get(escolha)

def menu_de_frutas(frutas):
    fs = list(enumerate(frutas))
    for (op, fruta) in fs:
        print("%d - %s" % (op, fruta))

    escolha = int(input("Digite a fruta desejada: "))

    return fs[escolha][1]

def checkout(quitanda, cesta):
    preco_total = 0

    for (fruta, quantidade) in cesta.items():
        preco_total += quitanda[fruta] * quantidade

    return preco_total

def main():
    while True:
        # pattern matching
        match menu_principal():
            case 'Ver cesta':
                print(cesta)

            case 'Adicionar fruta':
                fruta = menu_de_frutas(quitanda)
                cesta[fruta] += 1
                print("Fruta adicionada com sucesso")

            case 'Checkout':
                preco = checkout(quitanda, cesta)
                print(f"Total: ${preco:.2f}")

            case 'Sair':
                break

main()
