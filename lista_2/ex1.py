# -*- coding: utf-8 -*- 
#Exercio numero 1
#Faça um Programa que peça os três lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = float( input(" Insira o primeiro lado: "))
lado2 = float( input(" Insira o segundo lado: "))
lado3 = float( input(" Insira o terceiro lado: "))

if  lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
	print ("Não é triâgulo")
elif lado1 == lado2 == lado3:
	print ("Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
	print ("Isósceles")
else:
	print ("Escaleno")
