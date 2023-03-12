import random

def criaLista(n):
    l: [int] = [0 for x in range(0,n)]
    for i in range (0,n):
        l[i] = random.randint(1,100)
        if(l.count(l[i]) > 1):
            l[i] = random.randint(1,100)
    return l

def crescente(l):
    for i in range(0,len(l)-1):
        for j in range(len(l)-1):
            if(l[j]>l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

def decrescente(l):
    for i in range(0,len(l)-1):
        for j in range(len(l)-1):
            if(l[j]<l[j+1]):
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
    return l

n = int(input("Digite o tamanho da lista: "))
lista = criaLista(n)
print(f"Lista original = {lista}")
#crescente
lista = crescente(lista)
print(f"Lista em ordem crescente = {lista}")
#decrescente
lista = decrescente(lista)
print(f"Lista em ordem decrescente = {lista}")