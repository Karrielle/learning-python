# idade = int(input('Escreva sua idade: '))
# nome = input('Escreva seu nome: ')
# salario = float(input('Escreva seu salário: '))

# print(f'{nome} possui {idade} anos e recebe {salario} de salário')

# calculo = 7 / 2
# print(calculo)


# Inicialização de variáveis não é necessária aqui
# print('Entre com o primeiro número: ')
# x = int(input())

# print('Entre com o segundo número: ')
# y = int(input())

# # Realiza a soma
# z = x + y
# print(f'A soma dos números é {z}')
# z = x - y
# print(f'A subtração dos números é {z}')
# z = x * y
# print(f'A multiplicação dos números é {z}')
# z = x / y
# print(f'A div dos números é {z}')
# z = x % y
# print(f'O resto da divisão dos números é {z}')

# print('Cálculo do delta de uma equação do segundo grau\n')
# a = int(input('Digite o valor de a: '))
# b = int(input('Digite o valor de b: '))
# c = int(input('Digite o valor de c: '))

# print(f'Equação: {a}x² + {b}x + {c} = 0')

# delta = b * b - 4 * a * c
# print(f'o delta da equação é: {delta}')






# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# x = n1 == n2
# print(f'São iguais? {x} \n')

# z = n1 > n2
# print(f'{n1} É maior que {n2} ? {z} \n')


# y = n1 != n2
# print(f'São diferentes? {y} \n')




# from datetime import datetime, time

# # Definindo os turnos
# turnos = {
#     "01x07": (time(1, 0), time(7, 0)),
#     "07x13": (time(7, 0), time(13, 0)),
#     "13x19": (time(13, 0), time(19, 0)),
#     "19x01": (time(19, 0), time(1, 0)),
# }

# def checar_permissao(usuario_tipo):
#     # Obtém a hora atual
#     agora = datetime.now().time()
    
#     # Se for um administrador, permite sempre
#     if usuario_tipo.lower() == "administrador":
#         return True

#     # Verifica se o usuário operacional está no turno correto
#     for inicio, fim in turnos.values():
#         # Tratamento especial para o turno que passa pela meia-noite
#         if inicio < fim:  # Turnos normais
#             if inicio <= agora < fim:
#                 return True
#         else:  # Turno que cruza a meia-noite (ex: 19x01)
#             if inicio <= agora or agora < fim:
#                 return True

#     # Fora do horário permitido para usuários operacionais
#     return False

# # Exemplos de teste
# usuario = "operacional"  # Pode ser "operacional" ou "administrador"
# if checar_permissao(usuario):
#     print("Permissão concedida para alterar os dados.")
# else:
#     print("Permissão negada para alterar os dados.")




# j1 = 'f'
# j2 = 'f'
# j3 = 'f'


# estado = j1 == 'a' or j2 == 'a' or j3 == 'a'
# print(f'\n Alguma janela aberta? {estado}')
# alarme_desligado = not estado
# print(f'Alarme desligado? {alarme_desligado}')
# estado = j1 == 'a' and j2 == 'a' and j3 == 'a'
# print(f'\nTodas as janelas abertas? {estado}')


# if j1 == 'f':
#     print('Janela fechada')
# else:
#     print('janela aberta')


# a = 5
# b = 10
# c = 5
# d = 2
# j = 4
# f = True
# g = False


# print(a + b - c - d)
# print(a + b * d)
# print(d - (c + j ))
# print( f == g != False)
# print( f == g != False)
# print((f or f) and False or g)


#simples
# print('Vamos calcular a média')
# n1 = float(input('Entre com a primeira nota: '))
# n2 = float(input('Entre com a segunda nota: '))
# media = (n1 + n2) / 2


# if media >= 5 and media < 7:
#     print(f'Sua média foi {media}, Aluno aprovado!')
# else:
#     print('Aluno reprovado')


#composta
# print('Vamos calcular a média')
# n1 = float(input('Entre com a primeira nota: '))
# n2 = float(input('Entre com a segunda nota: '))
# media = (n1 + n2) / 2


# if media >= 7:
#     print(f'Sua média foi {media}, Aluno aprovado!')
# elif media > 5 and  media < 7:
#     print(f'Sua média é: {media} e você está de recuperação')
# else:
#     print('Aluno reprovado')


# import  math as m, calendar as c, datetime as d, time as t,  random as r

# print(m.pi)
# nome = str(input('\nDigite seu nome: '))
# print(f'\n {nome.upper()}')

# ano_atual = d.datetime.now().year

# print(f'\nEstamos no ano de {ano_atual}')


# for i in range(11):
#     print(i)
#     t.sleep(3)


# num = r.randint(1,100)
# print(num)

# lista = list(range(5,10))
# print(lista)

# lista = list(range(0, 10, 3))
# print(lista)


# for _ in range(100):
#     num = r.randint(0, 100)
#     print(num)

# num = 1

# while num <= 10:
#     print(num)
#     num += 1




# while True:
#     nome = input("Digite seu nome, ou 'x' para parar: ")
#     if nome == 'x':
#         break
#     print(f'Bem vindo, {nome}')
# print("Até logo!")


# for contador in range(1, 11):
#     print(f'{contador}')



# print("Gerar números da loteria.\n")
# vezes = input('Digite um número de vezes: ')
# for n in vezes:
#     numero = r.sample(range(1, 50), 5)
#     print(numero)



# print("Gerar números da loteria.\n")

# numeros = r.sample(range(1, 51), 5)
# print(sorted(numeros))


# import random

# def inicio():
#     print("Gerar números da loteria.\n")
#     vezes = int(input("Digite quantos números deseja gerar: "))

#     for n in range(vezes):
#         print(random.randint(1, 50), end=" ")

# inicio()

# def inicio():
#     for contA in range(1, 6):
#         print("Rodada " + str(contA) + "\n")
#         for contB in range(1, 6):
#             print(" Valor: " + str(contB) + "\n")

# inicio()

# import random

# def inicio():
#     print("Para sair do programa tecle 0")
#     while True:
#         quant = int(input("Quantos números deseja gerar? "))
#         if quant == 0:
#             break
#         for cont in range(1, quant + 1):
#             print(random.randint(1, 100))

# inicio()

# import numpy as np


# números = np.array([2,6,7,9,0,1,2,4,8], np.int16)

# print(type(números))
# print(números[-1])
# print(números.dtype) #padrão int32

# números[0] = 3
# print(números[0])
# # Array bidimensional com Numpy

# M = np.array([[1,3,5],[2,4,6],[3,5,7]])
# print(M)

# print(M[0,1])
# M[0,1] = 7
# print(M[0,1])

# #VISUALIZAR UMA COLUNA INTEIRA
# print(f'primeira coluna: {M[:,0]}')
# print(f'primeira coluna: {M[:,1]}')

# #VISUALIZAR UMA LINHA INTEIRA
# print(f'Segunda linha: {M[1,:]}')

# #NÚMERO DE DIMENSÕES DE UM ARRAY
# print(números.ndim)
# print(M.ndim)

# #TAMANHO DO ARRAY
# print(números.shape)
# print(M.shape)

# #NÚMEROS DE ELEMENTOS DE UM ARRAY
# print(números.size)
# print(M.size)


# # Solicita ao usuário para inserir os valores
# valores = input("Insira os valores separados por espaço: ")

# # Converte os valores inseridos em uma lista de números
# lista_valores = list(map(float, valores.split()))

# # Cria um array NumPy a partir da lista de valores
# array_valores = np.array(lista_valores)

# # Ordena o array
# array_ordenado = np.sort(array_valores)

# print("Array ordenado:", array_ordenado)


# def mostraMensagem():
#   print('Bóson Treinamentos em Tecnologia')
#   print('Curso de Lógica de Porgramação')


# mostraMensagem()

def calculoCubo(num):
    print('Cálculo do cubo de um número')
    c = num ** 3
    print(f'O Cubo é: {c}')


calculoCubo(7)