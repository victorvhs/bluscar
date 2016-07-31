# -*- coding: utf-8 -*- 
#Exercio numero 4
#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
#de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc

def fib(n):
	if n< 2:
		return n
	else:
		return fib(n-1)+fib(n-2)

nun = int( input("Insira um número: "))
print("Fibonacci de %2d é %2d" %(nun,fib(nun)))
