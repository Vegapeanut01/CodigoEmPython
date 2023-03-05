salario: float; novo: float; aumento: float
aumento: int

salario = float(input("Digite o salario da pessoa: "))

if salario <= 1000.00:
    porcentagem = 20
    aumento = salario * 0.20
    novo = salario + aumento
elif salario <= 3000.00:
    porcentagem = 15
    aumento = salario * 0.15
    novo = salario + aumento
elif salario <= 8000.00:
    porcentagem = 10
    aumento = salario * 0.10
    novo = salario + aumento
else:
    porcentagem = 5
    aumento = salario * 0.05
    novo = salario + aumento

print(f"Novo salario = R$ {novo:.2f}")
print(f"Aumento = R$ {aumento:.2f}")
print(f"porcentagem = {porcentagem} %")