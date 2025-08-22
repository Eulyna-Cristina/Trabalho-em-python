alturas = []
genero_masculino_alturas = []
genero_feminino_quantidade = 0

for i in range(1, 16):
    altura = float(input(f"Digite a altura da {i}ª pessoa: "))
    genero = input("Digite o gênero: ").strip().lower()
    alturas.append(altura)
    if genero == 'masculino':
        genero_masculino_alturas.append(altura)
    elif genero == 'feminino':
        genero_feminino_quantidade += 1

print("A maior altura é:", max(alturas))
print("A menor altura é:", min(alturas))
if genero_masculino_alturas:
    print("Média de altura dos homens:", sum(genero_masculino_alturas)/len(genero_masculino_alturas))
else:
    print("Nenhum homem informado.")
print("A quantidade de mulheres é:", genero_feminino_quantidade)