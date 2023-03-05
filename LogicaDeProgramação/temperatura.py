C: float; F: float;
temp: str

temp = str(input("Voce vai digitar a temperadura em qual escalha (C/F)? "))

if temp == 'F':
    F = float(input("Digite a temperatura em Fahrenheit: "))
    C = (5.0/9.0) * (F -32.0)
    print(f"Temperatura equivalente em Celsius: {C:.2f}")
else:
    C = float(input("Digitea a temperatura em Celsius: "))
    F = (C * (9.0/5.0)) + 32.0
    print(f"Temperatura equivalente em Fahrenheit: {F:.2f}")