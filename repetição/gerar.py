import random
i = 0
lista = []
while i <= 15:
         n = random.randint(10,100)
         for k in lista:
             if k != n:
             lista.append(n)
         i+=1
