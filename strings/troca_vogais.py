# -*- coding: utf-8 -*- 
#Exercio
#Faça um programa que leia uma palavra e troque vogais por "*"

palavra = input("Insira a palavra: ")

trocada = ""

for i in range(len(palavra)):
	if palavra[i] in 'aeiou':
		trocada = trocada + "*"
	else:
		trocada = trocada+palavra[i]
print(trocada)
