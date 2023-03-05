n: int; abaixo: int; entre: int; acima: int
totalCompra: float; totalVenda: float

n = int(input("Serao digitados dados de quatos produtos? "))

produto: [str] = [0 for x in range(n)]
Pcompra: [float] = [0 for x in range(n)]
Pvenda: [float] = [0 for x in range(n)]
percentual: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Produto {i+1}:")
    produto[i] = str(input(f"Nome: "))
    Pcompra[i] = float(input("Preco de compra: "))
    Pvenda[i] = float(input("Preco de venda: "))

#achando os lucro, abaixo, entre e acima
for i in range(0, n):
    percentual[i] = (Pvenda[i] - Pcompra[i] / Pcompra[i]) * 100

abaixo = 0
entre = 0
acima = 0
for i in range(0, n):
    if percentual[i] < 10.0:
        abaixo = abaixo + 1
    elif percentual[i] < 20.0:
        entre = entre + 1
    else:
        acima = acima + 1

#total de compra e venda
totalCompra = 0
totalVenda = 0
for i in range(0, n):
    totalCompra = totalCompra + Pcompra[i]
    totalVenda = totalVenda + Pvenda[i]

print()
print("RELATORIO:")
print(f"Lucro abaixo de 10%: {abaixo}")
print(f"Lucro entre 10% e 20%: {entre}")
print(f"Lucro acima de 20%: {acima}")
print(f"Valor total de compra: {totalCompra:.2f}")
print(f"Valor total de venda: {totalVenda:.2f}")
print(f"Lucro total: {totalVenda - totalCompra:.2f}")