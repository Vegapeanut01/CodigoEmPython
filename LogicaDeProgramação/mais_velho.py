n: int; maisvelho: int; posicao: int

n = int(input("Quantas pessoas voce vai digitar? "))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa:")
    nomes[i] = str(input("Nome: "))
    idades[i] = int(input("Idade: "))

maisvelho = idades[0]
for i in range(1, n):
    if idades[i] > maisvelho:
        maisvelho = idades[i]
        posicao = i

print(f"PESSOAS MAIS VELHA: {nomes[posicao]}")