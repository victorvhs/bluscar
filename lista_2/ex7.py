# -*- coding: utf-8 -*- 
#Exercio numero 7
#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.
from math import ceil
metros = float( input("Insira a metragem da área: "))

litros_tinta = metros /3
latas = ceil( litros_tinta /18)
preco = latas * 80

print("Litros de tinta:%5.2f" % litros_tinta)
print("Latas de tinta:%5.2f" % latas)
print("Preço R$ %5.2f" % preco)
