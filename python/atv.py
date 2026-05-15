def mostrar_produtos(produtos):
    print("\n===== PRODUTOS =====")

    for p in produtos:
        print(p)


def adicionar_produto(codigo, preco):

    match codigo:

        case 1:
            print("Macarrão adicionado!")
            preco += 3.20

        case 2:
            print("Arroz adicionado!")
            preco += 4.20

        case 3:
            print("Feijão adicionado!")
            preco += 4.50

        case 4:
            print("Açúcar adicionado!")
            preco += 8.20

        case 5:
            print("Queijo adicionado!")
            preco += 10.00

        case _:
            print("Produto inválido!")

    return preco


def aplicar_desconto(preco):

    if preco > 200 and preco < 500:
        desconto = preco * 0.05
        preco -= desconto

        print("\nVocê recebeu 5% de desconto!")

    elif preco >= 500:
        desconto = preco * 0.10
        preco -= desconto

        print("\nVocê recebeu 10% de desconto!")

    return preco


def finalizar_compra(preco):

    preco = aplicar_desconto(preco)

    print("\nSistema finalizado!")
    print(f"Total da compra: R$ {preco:.2f}")


def main():

    produtos = [
        "1 | Macarrão | Preço unitário: R$ 3,20",
        "2 | Arroz | Preço unitário: R$ 4,20",
        "3 | Feijão | Preço unitário: R$ 4,50",
        "4 | Açúcar | Preço unitário: R$ 8,20",
        "5 | Queijo | Preço unitário: R$ 10,00",
        "0 | Finalizar"
    ]

    preco = 0

    while True:

        mostrar_produtos(produtos)

        ler_pdt = int(input("Produto: "))

        if ler_pdt == 0:
            finalizar_compra(preco)
            break

        preco = adicionar_produto(ler_pdt, preco)

        print(f"Total atual: R$ {preco:.2f}")


main()
