
# -*- coding: UTF-8 -*-

# IMPORTAÇÕES
import os
import re

# LIMPANDO A TELA
def limpa_tela():
	os.system('cls') or None

# CADASTRAR UM NOVO NOME
def cadastrar(nomes):
	opcao = ''
	while(opcao != '0'):
		limpa_tela()
		print('---------- CADASTRO ----------')
		print('1 - Cadastrar novo nome')
		print('0 - Voltar')
		print('Escolha uma opção: ')
		opcao = input()
		if(opcao == '1'):	
			print('Digite o seu nome: ')
			nome = input()
			nomes.append(nome)
	

# LISTAR OS NOMES CADASTRADOS
def listar(nomes):
	limpa_tela()
	print('---------- LISTA ----------')
	print('Listando os nomes: ')
	opcao = ''
	while(opcao != '0'):
		for nome in nomes:
			print(nome)
		print('0 - Voltar: ')
		opcao = input()

# BUSCAR POR UM NOME
def buscar(nome):
	limpa_tela()
	letra_inicial = nome[0]
	resultados = re.findall(r'^'+ letra_inicial, nome)
	opcao = ''
	while(opcao != '0'):
		limpa_tela()
		print('Resultados encontrados: ')
		for resultado in resultados:
			print(resultado)
		print("1 - Fazer uma nova busca")
		print('0 - Voltar ao menu')
		print('Escolha uma opção: ')
		opcao = input()

# MENU DE OPÇÕES
def menu():
	nomes = []
	opcao = ''
	while(opcao != '0'):
		limpa_tela()
		print('---------- MENU ----------')
		print('1 - Cadastrar \n2 - Listar\n3 - Buscar \n0 - Sair')
		print('Escolha uma opção: ')
		opcao  = input()
		if(opcao == '1'):
			cadastrar(nomes)
		elif(opcao == '2'):
			listar(nomes)
		elif(opcao == '3'):
			print('Digite o nome a ser buscado: ')
			nome = input()
			buscar(nome)

# APP
menu()
