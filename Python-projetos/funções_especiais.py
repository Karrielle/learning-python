# FUNÇÕES LAMBDA (ANÔNIMAS): N TEM NOME E PODEM SER CRIADAS E USADAS NO MESMO MOMENTO
#ATALHO DE FUNÇÃO
#SINTAXE:
#LAMBDA ARGUMENTOS: EXPRESSÃO   


# quadrado = lambda x: x**2

# for i in range(1, 11):
#     print(quadrado(i))

# par = lambda x: x %2 == 0
# print(par(9))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))


#FUNÇÃO MAP() INTERNA PYTHON FUNÇÃO QUE APLICA FUNÇÕES, USADA COM LAMBDA GERALMENTE MAIS PODEROSAS E CURTINHAS
#SINTAXE
#map (função, iterável)   # a função pode ser lambda ou def

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2, num))
# print(dobro)

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# maiúsculas = list(map(str.upper, palavras))
# print(maiúsculas)

# FUNÇÃO filter() complemento de map

#sintaxe:
#filter(função, sequência)

# def numeros_pares(n):
#     return n % 2 == 0


# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_par = list(filter(numeros_pares, numeros))
# print(num_par)



#EXEMPLO COM LAMBDA
# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# num_impar = list(filter(lambda x: x %2 != 0, numeros))
# print(num_impar)


# FUNÇÃO reduce()  #precisa ser importada em um módulo retorna um valor só, total 
#sintaxe
#reduce (função, sequência, valor_inicial)

from functools import reduce

# def mult(x, y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# total = reduce(mult, numeros)
# print(total)


# Soma cumulativa dos quadrados de valores, usando expressão lambda

# numeros = [1,2,3,4]

# # ((1² + 2²)² + 3²)² + 4²


# total = reduce(lambda x, y: x**2 + y**2, numeros)
# print(total)


