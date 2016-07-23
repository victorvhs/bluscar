# -*- coding: utf-8 -*- 
#Exercio numero 
#Escreva um programa que leia um valor em metros
# e o exiba convertido em milímetros
#nota 1 metro = 1000 milímetros
print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

metros = float (input("Insira o valor em metros: "))
milimetros = metros * 1000

if( metros == 1 or metros ==0):
	plural = "metro"
else:
	plural = "metros"
print("%.2f %s em milímetros é %.2f" %(metros,plural,milimetros) )
