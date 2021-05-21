# Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
# se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
# sortudos existem entre 18644 e 33087, incluindo os extremos?

resposta = 0

for i in range(18643, 33088):
    num = str(i)
    if '2' in num and not '7' in num:
        resposta += 1

print("Existem ", resposta, " numero sortudos")
