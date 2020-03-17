#coding: utf-8
import sys

lista_acoes = [float(valor_acao) for valor_acao in sys.argv[1:]] # Lista contendo os valores das ações passadas pelo terminal
maior_lucro = 0 # Armazena o maior lucro
dia_compra_lucro = 0 # Armazena o dia da compra que gera o maior lucro
dia_venda_lucro = 0 # Armazena o dia da compra que gera o maior lucro

# Processamento
for dia_compra in range(0, len(lista_acoes)-1):
	# Iterar sobre a lista de ações, pivoteando o dia de compra
	for dia_venda in range(dia_compra+1, len(lista_acoes)):
		# Iterando os dias possiveis de venda, comprando no dia pivoteado
		lucro_iteracao = lista_acoes[dia_venda] - lista_acoes[dia_compra]
		if lucro_iteracao > maior_lucro:
			# Caso o lucro dessa iteração seja maior que o maior já armazenado, este se torna o maior lucro,
			# dessa forma ao final teremos o maior valor e os dias desejados.
			dia_venda_lucro = dia_venda
			dia_compra_lucro = dia_compra
			maior_lucro = lucro_iteracao

# Impressão dos resultados
if maior_lucro > 0:
	print('O melhor seria comprar no dia {}, vender no dia {} e se obtém um lucro de {}'.format(
		dia_compra_lucro+1, dia_venda_lucro+1, maior_lucro))
else:
	print('Não há possibilidade de lucro')
