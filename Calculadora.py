num1: int; num2: int; resultado: int
#operador: str

def soma():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o seguinte valor: "))
    return num1 + num2

def subtracao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o seguinte valor: "))
    return num1 - num2

def mutiplicacao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o seguinte valor: "))
    return num1 * num2

def divisao():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o seguinte valor: "))
    return num1 / num2





opcao = 0
while(opcao != '5'):
    print("Escolha uma das operações abaixo:")
    print("1 - soma")
    print("2 - subração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - Sair")
    opcao = input()
    if(opcao != 5):
        match opcao:
            case '1':
                resultado = soma()
                print(f"O resultado da operação foi: {resultado}\n")
            case '2':
                resultado = subtracao()
                print(f"O resultado da operação foi: {resultado}\n")
            case '3':
                resultado = mutiplicacao()
                print(f"O resultado da operação foi: {resultado}\n")
            case '4':
                resultado = divisao()
                print(f"O resultado da operação foi: {resultado}\n")



