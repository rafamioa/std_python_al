'''
ESPECIFICADA COM ASPAS SIMPLES '' OU ASPAS DUPLAS ""
SLICE - PEGA PARTE DE UMA STRING
'''

nome = 'Rafael'
nome_aluno = 'Ana Luiza da Silva'
idade = 20

print(nome, nome_aluno)
print(nome[0:4])	# SLICE

primeiro_nome = nome_aluno[0: 3]
print(primeiro_nome)

print('Meu nome é ' + nome)

#CONCATENANDO STRING COM OUTROS TIPOS DE DADOS
print('Nome do aluno(a): %s e idade: %d' % (nome_aluno, idade))


