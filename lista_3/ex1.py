# -*- coding: utf-8 -*- 
#Exercio numero 1
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
#seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
	nota = float( input("Insira um número de 0 a 10 \n: "))
	if nota >= 0 and nota <= 10:
		print("Nota %2.2f" %nota)
		break;
	else:
		print("Nota %2.2f é invalida" % nota )		
