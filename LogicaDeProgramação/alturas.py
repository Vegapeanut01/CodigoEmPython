n: int; menores: int
media: float; Pmenores: float; soma: float

n = int(input("Quantas pessoas serao digitadas? "))

nomes: [str] = [0 for x in range(n)]
idades: [int] = [0 for x in range(n)]
alturas: [float] = [0 for x in range(n)]

for i in range(0, n):
    print(f"Dados da {i+1}a pessoa:")
    nomes[i] = str(input("Nome: "))
    idades[i] = int(input("Idade: "))
    alturas[i] = float(input("Altura: "))

#altura media
print()
soma = 0
menores = 0
for i in range(0, n):
    soma = soma + alturas[i]
    if idades[i] < 16:
        menores = menores + 1

#media das alturas
media = soma / n
#pessoas com menos de 16
Pmenores = (menores / n) * 100.0

#imprimindo
print(f"Altura media: {media:.2f}")
print(f"Pessoas com menos de 16 anos: {Pmenores:.1f}%")
for i in range(0, n):
    if idades[i] < 16:
        print(nomes[i])