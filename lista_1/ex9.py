# -*- coding: utf-8 -*- 
#Exercio numero 9
#Escreva um programa que pergunte a quantidade de km percorridos por um carro 
#alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
#foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00
#por dia e R$ 0,15 por km rodado.

print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

PRECO_DIA = 60
PRECO_KM = 0.15

distacia_km = int( input("Insira a distancia percorrida em Km: "))
dias = int( input("Insira a quantidade de dias com o carro: "))

pagar = (dias * PRECO_DIA) + (distacia_km * PRECO_KM)

print ("Valor a pagar pelo carro é de R$ %.2f" %pagar)
