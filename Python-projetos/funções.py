# Funções é bloco de código que executa determinada tarefa // posso usar quantas vezes quiser ou importar em outros programas
#VANTAGENS: Modularização, Reúso de Código, Legibilidade


#como criar? 

# def <nome_função ([argumentos]):
#     <instruções>


# def mensagem():
#     print('Bóson Treinamentos em Tecnologia')
#     print('Curso Completo de Python.')

# def soma(a, b):
#     print(a+b)

# soma(12, 7)

# def mult(x, y):
#     return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f'O produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossível dividir por zero!'

# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')


# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados 

# if __name__ == '__main__':
#     valores = [2,5,7,9,12]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

# def contar(num=11, caractere='+'):  #quando tem parametro sem argumento, preciso colocar o argumento e ele tem que vim primeiro
#     for i in range(1, num):
#         print(caractere)
    
# if __name__ == '__main__':
#     contar(num=8, caractere='@') # posso colocar se estiver na ordem sem falar o parametro


x = 5
y = 6
z = 3

def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c
    
if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)


