x: int; produto: int

x = int(input("Deseja a tabuada para qual valor? "))

for i in range(1, 11):
    produto = x * i
    print(f"{x} x {i} = {produto}")