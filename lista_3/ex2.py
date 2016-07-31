# -*- coding: utf-8 -*- 
#Exercio numero 2
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

while True:
	user = input("Insira nome de usuário\n: ")
	senha = input("Insira senha\n: ")
	if user == senha:
		print("Usuário não pode ser igual a senha\nTente outra vez")
	else:
		print("Tudo ok")
		break
