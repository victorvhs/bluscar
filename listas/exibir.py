# -*- coding: utf-8 -*- 
#Ler 5 números inteiros e exibir o vetor

i = 0
vetor = []

while i < 5:
	nun= int( input("Insira o inteiro %d: "%(i+1)))
	vetor.append(nun)
	i+=1
print("O vetor é:",vetor)
