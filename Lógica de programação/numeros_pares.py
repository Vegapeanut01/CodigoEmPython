n: int; pares: int

n = int(input("Quantos numeros voce vai digitar? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

print()
pares = 0
print("NUMEROS PARES:")
for i in range(0, n):
    if  vet[i] % 2 == 0:
        pares = pares + 1
        print(vet[i], end="  ")

print("\n")
print(f"QUANTIDADE DE PARES = {pares}")