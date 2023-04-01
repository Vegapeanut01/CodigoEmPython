#força bruta
class Solucao:
    def doisSoma(self, nums: list[int], target: int) -> list[int]:
        for i in range (len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

    def criaLista(self,):
        n = int(input("Quantos elementos vai ter na lista? "))
        lista:  [int] = [0 for x in range(n)]
        for i in range(0, n):
            lista[i] = int(input("Digite um valor: "))
        return lista

#Usando Hash table / hash map
class solucao:
    def somadois(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complemento = target - nums[i]
            if complemento in hashmap and hashmap[complemento] != i:
                return [i, hashmap[complemento]]


p = Solucao()
s = solucao()

lista = p.criaLista()
desejado = int(input("Digite um valor que se deseja encontrar: "))

r = p.doisSoma(lista,desejado)
r2 = s.somadois(lista,desejado)

print("Fazendo na força brutra:")
print(f"\nOs indices que retornam o valor desejado são: {r}")
print("\nFazendo usando hash map:")
print(f"\nOs indices que retornam o valor desejado são: {r2}")
