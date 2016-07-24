# -*- coding: utf-8 -*- 
#Exercio numero 3
#Escreva um programa que leia a quantidade de dias, horas, 
#minutos e segundos do usuário. Calcule o total em segundos

print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

dia = int(input ("Insira os dias : "))
horas = int(input ("Insira as horas: "))
minutos = int(input ("Insira os minutos: "))
segundos = int(input ("Insira os segundos: "))

total_em_segundos = segundos + (minutos*60) +(horas * 3600) + (dia * 86400)
print ("Total em segundos é: %d"%total_em_segundos)
