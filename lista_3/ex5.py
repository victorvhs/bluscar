# -*- coding: utf-8 -*- 
#Exercio numero 5
#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando
#o algoritmo de Euclides. 

def mdc(a, b):
	while b !=0 :
		q = a / b
		r = a % b
		a = b
		b = r
	return a

nun1 = int( input("Insira o primeiro número: "))
nun2 = int( input("Insira o segundo número: "))

print( "O MDC é %5d"%mdc(nun1,nun2))
