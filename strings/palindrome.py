# -*- coding: utf-8 -*- 
#Exercio
#Verifique se uma palavra é palíndrome

palavra = input("Insira uma palavra\n: ")
palavra_invertida = palavra[::-1]

if palavra == palavra_invertida:
	print("Temos uma palavra PALÍNDROME")
	print(palavra)
else:
	print("%s não é Palíndrome" % palavra )
	
