# -*- coding: utf-8 -*- 
#Ler um vetor de 10 números inteiros e imprimir a ordem inversa

i = 0
vetor = []
while i <= 9:
	nun = int( input ("Insira o número %d: "%(i+1)))
	vetor.append(nun)
	i +=1

print(i)
i = 9
while i >= 0:
	print("Elemento %d : %d" %((i+1), vetor[i]))
	i-=1
	

