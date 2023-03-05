n: int
soma: float; media: float

n = int(input("Quanto numeros voce vai digitar? "))

vet: [float] = [0 for x in range(n)]

for i in range(0, n):
    vet[i] = float(input("Digite um numero: "))

#soma e media
soma = 0
for i in range(0, n):
    soma = soma + vet[i]

media = soma / n


#imprimindo
print()
print("VALORES = ", end="")
for i in range(0, n):
    print(vet[i], end="  ")

print()
print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")