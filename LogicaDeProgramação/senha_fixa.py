senha: int

senha = int(input("Digite a senha: "))

while senha != 2002:
    senha = int(input("Senha invalida! Tente novamente: "))

print("Acesso permitido!")