# -*- coding: utf-8 -*- 
#Exercio
# Trocar as vogais por *

msg = open('mensagem.txt','r')
crip = open('crip.txt','w')

for linhas in msg.readlines():
	for letra in linhas:
		if letra in 'aeiou':
			crip.write("*")
		else:
			crip.write(letra)
msg.close()
crip.close()
