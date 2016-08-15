import urllib.request
"""
    Programa simples para pegar a cotação do cafe e a data.
"""
pg = urllib.request.urlopen('http://beans.itcarlow.ie/prices.html')
texto = pg.read().decode('utf8')

preco = texto[234:238]
data = texto[290:309]
cotacao = {data:preco}

print(cotacao)