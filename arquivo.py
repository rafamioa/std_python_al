import os

def limpa_tela():
	os.system('cls') or None

# CLASSE USUÁRIO
class Usuario(object):
	'Classe modelo usuário'
	def __init__(self, login, senha):
		self.login = login
		self.senha = senha

	def imprimir(self):
		print('Login: \t%s\nSenha: \t%s' % (self.login, self.senha))
		print('---------------------------------')

# FUNÇÃO DE CADASTRAR
def cadastrar():
	limpa_tela()
	print('********** CADASTRO DE USUÁRIOS **********')
	print('Digite o login: ')
	login = input()
	print('Digite a senha: ')
	senha = input()
	Usuario(login, senha)
	file = open('usuarios.txt', 'a')
	file.write(login + ',' + senha + '\n')
	file.close()

def listar():
	file = open('usuarios.txt', 'r')
	usuarios = []
	for usuario in file:
		resultados = usuario.split(',')
		usuario = Usuario(resultados[0], resultados[1])
		#usuarios.append(Usuario(*resultados))
		usuarios.append(usuario)
	file.close()
	return usuarios

def buscar():
	opcao = ''
	while opcao != '0':
		limpa_tela()
		print('Digite o login: ')
		login = input()
		usuarios = listar()
		for usuario in usuarios:
			if usuario.login == login:
				print('Usuário encontrado')
				print(usuario.imprimir())
				break
		print('1 - Nova busca\n0 - Voltar')
		print('Escolha uma opção: ')
		opcao = input()
	


def imprimir_lista(usuarios):
	limpa_tela()
	print('********* LISTA DE USUÁRIOS CADASTRADOS **********')
	opcao = ''
	for usuario in usuarios:
		usuario.imprimir()	
	while(opcao != '0'):				
		print('Digite 0 para voltar: ')
		opcao = input()

# MENU
def menu():
	opcao = ''
	while(opcao != '0'):
		limpa_tela()
		print('********** MENU DO SISTEMA **********')
		print('1 - Cadastrar \n2 - Listar\n3 - Buscar\n0 - Sair\nEscolha uma opcao: ')
		opcao = input()
		if opcao == '1':
			cadastrar()
		elif opcao == '2':
			usuarios = listar()
			imprimir_lista(usuarios)
		elif opcao == '3':
			buscar()
		else:
			print('Informe uma opção válida')

# APP
menu()