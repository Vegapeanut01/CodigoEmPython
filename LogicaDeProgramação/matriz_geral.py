import math

n: int; linha: int; coluna: int
soma: float;

n = int(input("Qual a ordem da matriz? "))

mat: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

print("")
#soma dos positivos
soma = 0
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]

print(f"SOMA DOS POSITIVOS: {soma:.1f}")
print()
#imprindo uma linha
linha = int(input("Escolha uma linha: "))
print("LINHA ESCOLHIDA:", end=" ")
for j in range(0, n):
    print(f"{mat[linha][j]:.1f}", end=" ")
print("\n")

#impridindo uma coluna
coluna = int(input("Escolha uma coluna: "))
print("COLUNA ESCOLHIDA:",end=" " )
for i in range(0, n):
    print(f"{mat[i][coluna]:.1f}", end=" ")
print("\n")

#diagonal principal
print("DIAGONAL PRINCIPAL: ", end=" ")
for i in range(0, n):
    print(f"{mat[i][i]:.1f}", end=" " )

print("\n")
#matriz alterada
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            mat[i][j] = math.pow(mat[i][j],2)

#imprimindo a matriz alterada
print("MATRIZ ALTERADA:")
for i in range(0, n):
    for j in range(0, n):
        print(f"{mat[i][j]:.1f}", end=" ")
    print()