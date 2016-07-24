# -*- coding: utf-8 -*- 
#Exercio numero 8
#Converta uma temperatura digitada em  Fahrenheit para Celsius. 
#temp_c = (temp_f-32)/1.8


print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

temp_f = float( input("Insira a tempereratura em Fahrenheit: "))
temp_c = (temp_f-32) / 1.8

print ("%.2f Fahrenheit = %.2f Celsius" %(temp_f, temp_c))
