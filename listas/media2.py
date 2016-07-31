# -*- coding: utf-8 -*-
# Ler 4 notas, mostrar a media e as notas

notas = []
soma = 0
i = 0

while i <= 3:
	nun = float( input("Insira a nota %d:" %(i+1)))
	notas.append(nun)
	soma += notas[i]
	i+=1

media = soma /i
print("A média é : %5.2f" % media)
print("Notas : ", notas)
