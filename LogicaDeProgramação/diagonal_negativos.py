n: int; negativos: int

n = int(input("Qual a ordem da matriz? "))

mat: [[int]] = [[0 for x in range(n)] for x in range(n)]

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))


#numero de negativos
negativos = 0
for i in range(0, n):
    for j in range(0, n):
        if mat[i][j] < 0:
            negativos = negativos + 1

#imprimindo
print("DIAGONAL PRINCIPAL:")
for i in range(0, n):
    print(mat[i][i], end= "  ")

print()
print(f"QUANTIDADE DE NEGATIVOS = {negativos}")

