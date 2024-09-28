# Dicionários permitem armazenar dados em pares chaves valor e são simliares aos arrays. não permitem item duplicados mas podem ser de qualquer tipo

#criando para armazenar inf de elementos quimicos

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

# não pode ter mais de um valor pra mesma chave, n pode chaves repetidas, chaves são imutáveis, listas nao pode utilizar

print(f'Elemento:  {elemento['nome']}')
print(f'Densidade:  {elemento['densidade']}')

print(f'O dicionário possui {len(elemento)} elementos')


#Atualizar ou modificar uma entrada do dic
elemento['grupo'] = 'Alcalinos'
print(elemento)

#Adicionar uma entra
elemento['periodo'] = 1
print(elemento)

#Exclusão de itens em dicionários
# del elemento['periodo']
# print(elemento)

# elemento.clear()
# print(elemento)

# del elemento
# print(elemento) #uteis para armazenar par, prenchimento de formularios, chegar no servidor assim  nome/senha/ valor oq digitaram

print(elemento.items())
for i in elemento.items():
    print(i)

print(elemento.keys())
for i in elemento.keys():
    print(i)

print(elemento.values())
for i in elemento.values():
    print(i)
    

#DESEMPACOTAR SEPARADAMENTE
for i, j in elemento.items():
    print(f'{i}: {j}')
