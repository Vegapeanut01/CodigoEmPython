n: int; mulheres: int
maior: float; menor: float; mediaAltura: float; altuarasoma: float

n = int(input("Quantas pessoas serao digitadas? "))

alturas: [float] = [0 for x in range(n)]
genero: [str] = [0 for x in range(n)]

for i in range(0, n):
    alturas[i] = float(input(f"Alutura da {i+1}a pessoa: "))
    genero[i] = str(input(f"Genero da {i+1}a pessoa: "))


#achando menor e maior
menor = alturas[0]
maior = alturas[0]
for i in range(1, n):
    if alturas[i] < menor:
        menor = alturas[i]

    if alturas[i] > maior:
        maior = alturas[i]

#media da mulheres
alturasoma = 0
mulheres = 0
for i in range(0, n):
    if genero[i] == "F":
        mulheres = mulheres + 1
        alturasoma = alturasoma + alturas[i]


mediaAltura = alturasoma / mulheres

#imprimindo
print(f"Menor altura = {menor:.2f}")
print(f"Maior altura = {maior:.2f}")
print(f"Media das alturas das mulheres = {mediaAltura:.2f}")
print(f"Numero de homens: {n - mulheres}")