m: int; n: int

m = int(input("Quantas linhas vai ter cada matriz? "))
n = int(input("Quantas colunas vai ter cada matriz? "))

matA: [[int]] = [[0 for x in range(n)] for x in range(m)]
matB: [[int]] = [[0 for x in range(n)] for x in range(m)]
matC: [[int]] = [[0 for x in range(n)] for x in range(m)]

#matriz A
print("Digite os elementos da matriz A:")
for i in range(0, m):
    for j in range(0, n):
        matA[i][j] = int(input(f"Elemento [{i},{j}]: "))

#matriz B
print("Digite os elementos da matriz B:")
for i in range(0, m):
    for j in range(0, n):
        matB[i][j] = int(input(f"Elemento [{i},{j}]: "))

#matriz C
for i in range(0, m):
    for j in range(0, n):
        matC[i][j] = matA[i][j] + matB[i][j]

#Imprindo
print("MATRIZ SOMA: ")
for i in range(0, m):
    for j in range(0, n):
        print(matC[i][j], end= "  ")
    print()