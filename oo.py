# -*- encoding: UTF-8 -*-

# CLASSE PERFIL
class Perfil(object):
	# DESCRIÇÃO DA CLASSE
	'Classe modelo para perfil'
	# CONSTRUTOR DA CLASSE
	def __init__(self, nome, empresa, telefone):
		self.nome = nome
		self.empresa = empresa
		self.telefone = telefone
		self.__curtidas = 0		# ATRIBUTO PRIVADO

	def imprimir(self):
		print('Nome: 		%s' % self.nome)
		print('Empresa: 	%s' % self.empresa)
		print('Telefone:	%s' % self.telefone)
		print('Curtidad:	%d' % self.get_curtidas())

	def curtir(self):
		self.__curtidas += 1

	def get_curtidas(self):
		return self.__curtidas

# CLASSE VIP
class Perfil_Vip(Perfil):
	'Classe perfil vip'
	def __init__(self, nome, empresa, telefone, apelido):
		super(Perfil_Vip, self).__init__(nome, empresa, telefone)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).get_curtidas() * 10

# APP
#perfil = Perfil('Rafael', 'FATEC', '0000-0000')
perfil = Perfil_Vip(nome='Rafael', empresa='FATEC', telefone='0000-0000', apelido='Rafa')
for i in range(0, 10):
	perfil.curtir()
perfil.imprimir()
print(perfil.apelido)
print(perfil.obter_creditos())