codigo: int; alcool: int; gasolina: int; diesel: int; x: int

x = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

alcool = 0
gasolina = 0
diesel = 0

while x != 4:
    match x:
        case 1:
            alcool = alcool + 1
        case 2:
            gasolina = gasolina + 1
        case 3:
            diesel = diesel + 1

    x = int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")