n: int; posicao: int
maior: float

n = int(input("Quantos numeros voce vai digitar? "))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

#achando o maior
maior = vet[0]
for i in range(1, n):
    if vet[i] > maior:
        maior = vet[i]
        posicao = i

print()
print(f"MAIOR POSICAO = {maior:.1f}")
print(f"POSICAO DO MAIOR VALOR = {posicao}")