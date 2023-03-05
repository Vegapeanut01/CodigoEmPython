minutos: int
plano: float;

plano = 50.00

minutos = int(input("Digite a quantidade de minutos: "))

if minutos > 100:
    plano = plano + (minutos - 100) * 2

print(f"Valor a pagar: R$ {plano:.2f}")
