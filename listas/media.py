# -*- coding: utf-8 -*- 
#Média de 5 numeros dentro de uma lista

notas = [10,10,10,10,10]
soma = 0
i = 0

while i < 5:
	soma = soma + notas[i] 
	i+=1

media = soma / i
print( "Media %5.2f" %media)
