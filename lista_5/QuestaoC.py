# Entre 1067 e 3627 (inclusive), quantos números são pares e também
# divisíveis por 7?

resposta = 0

for i in range(1067, 3628):
    if i % 2 == 0 and i % 7 == 0:
        resposta += 1

print(resposta)
