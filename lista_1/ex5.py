# -*- coding: utf-8 -*- 
#Exercio numero 5
#Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço a pagar

print ("Coletânea de atividades do curso Python para zumbis")
print("=========================")

preco = float( input("Insira o valor da mercadoria R$: "))
desconto_perc = float( input("Insira o percentual de desconto %: "))

desconto = preco * (desconto_perc/100)
preco_novo = preco - desconto

print ("Preço a pagar R$ %.2f. O desconto foi de R$ %.2f" %(preco_novo,desconto))
