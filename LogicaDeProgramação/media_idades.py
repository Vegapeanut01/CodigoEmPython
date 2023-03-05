x: int; soma: int; n: int
media: float

soma = 0
n = 0

print("Digite as idades: ")
x = int(input())

while x > 0:
    soma = soma + x
    n = n + 1
    x = int(input())

if n == 0:
    print("IMPOSSIVEL CALCULAR")
else:
    media = soma / n
    print(f"MEDIA = {media:.2f}")