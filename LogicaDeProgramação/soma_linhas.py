n: int; m: int
soma: float

n = int(input("Qual a quantidade de linhas da matriz? "))
m = int(input("Qual a quantidade de colunas da matriz? "))

vet: [float] = [0 for x in range(n)]
mat: [[float]] = [[0 for x in range(m)] for x in range(n)]

for i in range(0, n):
    print(f"Digite os elementos da {i+1}a. linha: ")
    for j in range(0, m):
        mat[i][j] = float(input())

#somando as linhas

for i in range(0, n):
    soma = 0
    for j in range(0, m):
        soma = soma + mat[i][j]
    vet[i] = soma


print("VETOR GERADO:")
for i in range(0, n):
    print(vet[i])