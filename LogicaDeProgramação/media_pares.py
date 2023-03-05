n: int; pares: int; soma: int
media: float

n = int(input("Quanto elementos vai ter o vetor? "))

vet: [int] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = int(input("Digite um numero: "))

#fazendo a media dos pares
pares = 0
soma = 0
for i in range (0, n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        pares = pares + 1

if pares == 0:
    print("NENHUM NUMERO PAR")
else:
    media = soma / pares
    print(f"MEDIA DOS PARES = {media:.1f}")