# -*- coding: utf-8 -*- 
#Exercio numero 10
#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias

print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

cigarro_dia = int( input("Insira a quantidade de cigarros fumandos por dia: "))
ano_fumante = int( input("Insira quantos anos você fumou: "))

tempo_min = ((ano_fumante * 365) * cigarro_dia)* 10
tempo_hr = tempo_min/60
tempo_dia = tempo_hr/24

print("Foram perdidos %.2f dias"%tempo_dia)
