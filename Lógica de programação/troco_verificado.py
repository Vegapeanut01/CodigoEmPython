preco: float; dinheiro: float; troco: float; falta: float
qtd: int

preco = float(input("Preco unitario do produto: "))
qtd = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

troco = dinheiro - (qtd * preco)
falta = (qtd * preco) - dinheiro

if troco < (qtd * preco):
    print(f"DINHEIRO INSUFICIENTE. FALTAM {falta:.2f} REAIS")
else:
    print(f"TROCO = {troco}")