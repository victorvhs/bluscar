# -*- coding: utf-8 -*- 
#Exercio numero 4
#Faça um Programa que leia três números e mostre o maior deles.

nun1 = int( input(" Número 1: "))
nun2 = int( input(" Número 2: "))
nun3 = int( input(" Número 3: "))
maxi = 0

if nun1 >= nun2 and nun1 >= nun3 :
	maxi = nun1
elif nun2 > nun3:
	maxi = nun2
else:
	maxi = nun3
	
print ("Maior número é %d"%maxi)
print ("Maior da função %d"%max(nun1,nun2,nun3))
