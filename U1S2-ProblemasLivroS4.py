#01
""""
lista: [int] = [0 for x in range(10)]
for i in range(0, 10):
    lista[i] = int(input(f"Digite um valor para posição {i+1}: "))

lista.reverse()

for i in range(0, 10):
    print(lista[i])
"""
#02
"""
lista1: [int] = [0 for x in range(10)]
lista2: [int] = [0 for x in range(10)]
lista3 = []
print("Digite os elementos da primeia lista!")
for i in range(0, 10):
    lista1[i] = int(input(f"Digite um valor para posição {i+1}: "))

print()
print("Digite os elementos da segunda lista!")
for i in range(0, 10):
    lista2[i] = int(input(f"Digite um valor para posição {i+1}: "))

lista3.extend(lista1)
lista3.extend(lista2)

print()
print("Terceira lista: ")
print(lista3)
print(f"Comprimento da terceira lista:  {len(lista3)}")
"""

#03
"""
A = [16, 8, 25, 12, 19]

B = [5, 14, 3, 27, 8, 21, 44]

R = []

R.extend(A)
R.extend(B)

print(len(R))
"""
#04
"""
n = int(input("Digite um tamanho para a lista: "))
lista: [int] = [0 for x in range(n)]

for i in range(0, n):
    lista[i] = int(input(f"Digite um número para posição {i+1}: "))
    if lista.count(lista[i]) > 1:
        lista[i] = int(input("Número já digitado, digite outro valor: "))


print()
print(f"Lista Digitada: {lista}")
"""
#05

nA = int(input("Digite o número de elementos da lista A: "))
nB = int(input("Digite o número de elementos da lista B: "))

print()

A: [int] = [0 for x in range(nA)]
B: [int] = [0 for x in range(nB)]

print("Digite os valores da lista A:")
print()
for i in range(0, nA):
    A[i] = int(input(f"Digite um número para posição {i+1}: "))
    if A.count(A[i]) > 1:
        A[i] = int(input("Número já digitado, digite outro valor: "))


print()
print("Digite os valores da lista B:")
print()
for i in range(0, nB):
    B[i] = int(input(f"Digite um número para posição {i+1}: "))
    if B.count(B[i]) > 1:
        B[i] = int(input("Número já digitado, digite outro valor: "))

print()

R = A + B

resultado = []

for i in R:
    if i not in resultado:
        resultado.append(i)


print(str( resultado))