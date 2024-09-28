#Lista: representa uma sequência de valores 

#Sintaxe: nome_lista =[]

# notas = [5,7,8,6,9]
# print(type(notas))

# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,4]
# valores = n1 + n2
# valores[0] = 9
# print(valores)
# print(type(valores[0]))
# print(valores[0:2]) # a partir do zero quantos?
# print(valores[:2])  #acessar 2
# print(valores[2:2])  #vazio

# #saber tamanho 
# print(len(valores))

# #versão ordenada se modificar e começar inverso
# print(sorted(valores, reverse=True))

# #somar valores da pra ver min e max 
# print(sum(valores))

# #adicionar no ultimo
# valores.append(13)
# print(valores)

# #retirar ultimo ou qualquer posição
# valores.pop(3)
# print(valores)

# #inserir em qualquer posição precisa de 2 argumentos posição e valor
# valores.insert(3, 21)
# print(valores)

# #verificar se tem valor na lista retorna boolean
# print(17 in valores)


#LISTA COM LAÇO

# planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno'] #list() criar vazia
# for planeta in planetas:
#     print(planeta)

# bebidas = print(input('Digite bebidas favoritas: '))
# for i in bebidas:
    
bebidas = []

for i in range(5):
    print(f'Digite uma bebida favorita:')
    bebida = input()
    bebidas.append(bebida)

bebidas.sort()
print(f'\nBebidas escolhidas:')
for bebida in bebidas:
    print(bebida)

print(f'\nSaúde!')