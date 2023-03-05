n: int
media: float; soma: float

n = int(input("Quanto elementos vai ter o vetor? "))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

#fazendo a media
soma = 0
for i in range(0, n):
    soma = soma + vet[i]

media = soma / n

#imprimindo
print()
print(f"MEDIA DO VETOR = {media:.3f}")
print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(0, n):
    if vet[i] < media:
        print(vet[i])
