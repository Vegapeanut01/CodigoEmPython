codigo: int; qtd: int;
valorPagar: float

codigo = int(input("Codigo do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

match codigo:
    case 1:
        valorPagar = 5.00 * qtd
    case 2:
        valorPagar = 3.50 * qtd
    case 3:
        valorPagar = 4.80 * qtd
    case 4:
        valorPagar = 8.90 * qtd
    case 5:
        valorPagar = 7.32 * qtd

print(f"Valor a pagar: R$ {valorPagar:.2f}")
