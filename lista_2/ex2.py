# -*- coding: utf-8 -*- 
#Exercio numero 2
#Determine se um ano é bissexto

ano = int( input("Digite o ano a ser verificado: "))

if ano % 400 == 0:
	print ("%d é um ano bissexto" %ano)
elif ano % 4 == 0:
	if ano % 100 != 0:
		print ("%d  é um ano bissexto" %ano)
	else:
		print ("%d não é um ano bissexto" %ano)
else:
	print ("%d não é um ano bissexto" %ano)
	
