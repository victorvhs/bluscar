# -*- coding: utf-8 -*- 
#Exercio
# Faça um programa que solicite a data de nascimento
#(dd/mm/aaaa) e imprima o nome do mês por extenso.

meses= ["Janeiro","Feveriro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novenbro", "Dezembro"]
data = input("Insira a data de nascimento\n(dd/mm/aaaa): ")

data = data.split('/')
"""
i = 1
while True:
	if int(data[1]) == i:
		data[1] = meses[i-1]
		break
	i+=1
"""
print("%s de %s de %s"%(data[0], meses[(int(data[1])-1)], data[2]))
