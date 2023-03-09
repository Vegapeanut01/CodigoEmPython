'''
def soma(num1, num2):
    return num1 + num2

a = int(input("Digite um número:  "))
b = int(input("Digite um número:  "))

resultado = soma(a,b)
print(f"\nResultado = {resultado}")
'''

'''
def igual_ou_nao(num1, num2):
    if num1 == num2:
       return "Os valores são iguais!"
    else:
        return "os numeros são diferentes"

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

resultado = igual_ou_nao(a,b)
print(resultado)
'''


def calculadora(num1, operador, num2):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2
    else:
        print("Operador inválido! Tente novamente")
        return 0


num1 = float(input("Digite um número: "))
operador = input(f"Escolha uma operação: '+' para soma, '-' para subutração, '*' para multiplicação ou '/' para divisão: ")
num2 = float(input("Digite outro número: "))

print(f"\nA operação a ser realizada vai ser: {num1} {operador} {num2}")

resultado = calculadora(num1, operador, num2)

print(f"\nResultado da operação: {resultado}")


