# -*- coding: utf-8 -*- 
#Exercio
#Imprima media de 10 inteiros

soma = 0
i = 1

while i <= 10:
	nun = int( input("Insira o numero %d: "%i))
	soma = soma + nun
	i=i+1
	
media = soma / 10
print (i)
print ("Média : %5.2f" %media)
