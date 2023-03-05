glicose: float

glicose = float(input("Digite a medida da glicose: "))

print("Classificacao: ", end="")

if glicose <= 100.0:
    print("normal")
elif glicose <= 140.0:
    print("elevado")
else:
    print("diabetes")