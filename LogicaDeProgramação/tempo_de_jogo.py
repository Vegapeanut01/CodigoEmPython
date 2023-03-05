horaInicial: int; horaFinal: int; duracao: int

horaInicial = int(input("Hora inicial: "))
horaFinal = int(input("Hora final: "))

if horaInicial < horaFinal:
    duracao = horaFinal - horaInicial
else:
    duracao = (horaFinal - horaInicial) + 24

print(f"O JOGO DUROU {duracao} HORA(S)")