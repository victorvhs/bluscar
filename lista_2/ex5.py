# -*- coding: utf-8 -*- 
#Exercio numero 4
#Faça um Programa que leia três números e mostre o maior e o menor deles.

nun1 = int( input(" Número 1: "))
nun2 = int( input(" Número 2: "))
nun3 = int( input(" Número 3: "))

if nun1 >= nun2 and nun1 >= nun3 :
	maxi = nun1
elif nun2 > nun3:
	maxi = nun2
else:
	maxi = nun3

if nun1 <= nun2 and nun1 <= nun3 :
	mini = nun1
elif nun2 < nun3:
	mini = nun2
else:
	mini = nun3


print ("Maior número é %d" %maxi)
print ("Maior da função %d" %max(nun1,nun2,nun3))

print ("Menor número é %d"  %mini)
print ("Menor da função %d" %min(nun1,nun2,nun3))
