'''
LISTA É UMA ESTRUTURA DE DADOS NÃO TIPADA
APPEND() - FUNÇÃO ADICIONAR ELEMENTO
REMOVE() - FUNÇÃO DE REMOVER ELEMENTO
'''
convites = ['Rafael','Ana', 'José']
print(convites)

#IMPRIMINDO OS ELEMENTOS DA LISTA
for i in convites:
	print(i)

#IMPRIMINDO PELA POSIÇÃO DO ELEMENTO
print(convites[0])
print(convites[1:])
print(convites[0:len(convites)])
print('Total de elementos: %d' % len(convites))
print('Total de elementos: ' + str(len(convites)))

#OPERAÇÕES COM LISTAS
convites.append('Joana')
convites.append('Marcelo')
print('Todos convites: %s' % (convites))
convites.remove('Rafael')
print('Todos convites: %s' % (convites))


