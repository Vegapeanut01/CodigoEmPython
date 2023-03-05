n: int; total: int; cobaia: int; coelhos: int; ratos: int; sapos: int
pcoelhos: float; pratos: float; psapos: float
tipo: str

n = int(input("Quantos casos de teste serao digitados? "))

coelhos = 0
ratos = 0
sapos = 0
for i in range(0, n):
    cobaia = int(input("Quantidade de cobaias: "))
    tipo = str(input("Tipo de cobaia: "))

    match tipo:
        case 'C':
            coelhos = coelhos + cobaia
        case 'R':
            ratos = ratos + cobaia
        case 'S':
            sapos = sapos + cobaia

total = coelhos + ratos + sapos
pcoelhos = (coelhos/total) * 100
pratos = (ratos/total) * 100
psapos = (sapos/total) * 100

print("")
print("RELATORIO FINAL: ")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {pcoelhos:.2f}")
print(f"Percentual de ratos: {pratos:.2f}")
print(f"Percentual de sapos: {psapos:.2f}")