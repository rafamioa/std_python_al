
def subtracao(a, b):
	r = a - b
	resultado(r) 

def soma(a, b):
	r =  a + b
	resultado(r) 

def multiplicacao(a, b):
	r = a * b
	resultado(r)

def divisao (a, b):
	r = a / b
	resultado(r)

def potencia(n, e):
	r = n ** e
	resultado(r)

def resto(n, e):
	r = n % e
	resultado(r)

def resultado(r):
	print('Resultado: %d' % r)

# FATORIAL RECURSIVO
def fat(n):
  if n <= 1:
    return 1
  return fat(n-1) * n

# IMPRIME OS RESULTADOS
multiplicacao(6,3)
print(fat(5))



