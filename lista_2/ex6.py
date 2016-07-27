# -*- coding: utf-8 -*- 
#Exercio numero 5
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:
#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

s_hr = float( input("Digite seu salario por hora: "))
hr_mes = int( input("Digite horas trabalhadas no mês: "))

sal_bruto = s_hr * hr_mes
ir = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto *0.05
sal_liquido = sal_bruto - ir - inss - sindicato

print("Salário bruto R$ %5.2f" % sal_bruto)
print("IR (11%%): R$ %5.2f" % ir)
print("Inss (8%%): R$ %5.2f" % inss)
print("Sindicato (5%%) R$ %5.2f" % sindicato)
print("Salário liquido R$ %5.2f" % sal_liquido)
