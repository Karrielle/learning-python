import random

# valor = random.randint(1,20)
# print(valor)

# print('Gerar cinco números aleatórios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Número gerado: {n}')

#FLOAT 
# valor = random.random()
# print(f'Número gerado: {round(valor * 10, 2)}')

# valor = random.uniform(1,100)
# print(f'Número: {round(valor, 4)}')

#ESCOLHER
L = [2,4,6,9,10,13,14,16,18,20,21,27,33]
# n= random.choice(L)
# print(f'Número escolhido: {n}')


# n = random.sample(L, 3)
# print(f'Números extraídos: {n}')


# EMBARALHAR
print(f'Exibir a lista original: {L}:')
print(f'Embaralhar a lista e exibi-la:')
n = random.shuffle(L)
print(L)

