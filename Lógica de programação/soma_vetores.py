n: int

n = int(input("Quanto valores vai ter cada vetor? "))

vetA: [int] = [0 for x in range(n)]
vetB: [int] = [0 for x in range(n)]
vetC: [int] = [0 for x in range(n)]

print("Digite os valores do vetor A:")
for i in range(0, n):
    vetA[i] = int(input())

print("Digite os valoes do vetor B:")
for i in range(0, n):
    vetB[i] = int(input())

#vetor C = resultado da soma
for i in range(0, n):
    vetC[i] = vetA[i] + vetB[i]

#imprimindo
print("VETOR RESULTANTE:")
for i in range(0, n):
    print(vetC[i])

