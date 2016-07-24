# -*- coding: utf-8 -*- 
#Exercio numero 6
#Calcule o tempo de uma viagem de carro. 
#Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 
# vel= espaço/tempo
#tempo = espaco*vel
print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

distancia = float( input("Insira a distância em km: "))
velocidade = float( input("Insira o tempo em km/hr: "))

tempo = distancia / velocidade

print ("O tempo de viagem foi %.1f horas"% tempo)

