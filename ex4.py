# -*- coding: utf-8 -*- 
#Exercio numero 
#Faça um programa que calcule o aumento de um salário. Ele deve solicitar 
#o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

salario = float( input("Insira o salario: "))
aumento_perc = float( input("Insira o percentual de aumento: "))

aumento = salario * (aumento_perc/100)
salario_novo = salario + aumento
print("Salario novo R$ %.2f com aumento de R$ %.2f" %(salario_novo, aumento))
