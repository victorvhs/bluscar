# -*- coding: utf-8 -*- 
#Exercio numero 3
#Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa
#anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de
#crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
#necessários para que a população do país A ultrapasse ou iguale a população do país B,
#mantidas as taxas de crescimento

pais_A = 80000
pais_B = 200000
taxa_A = 0.03
taxa_B = 0.015
i = 1
while True:
	pais_A = (pais_A * taxa_A) + pais_A
	pais_B = (pais_B* taxa_B) + pais_B
	
	print("Ano %d\nPaís A: %10d \nPaís B: %10d\n" %(i,pais_A,pais_B))
	i+=1
	if pais_A >= pais_B:
		print("População do país A se igualou ou superou País B")
		print("Ano %10d\nPaís A: %10d \nPaís B: %10d" %(i,pais_A,pais_B))
		break
