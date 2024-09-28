# # diferença de tuplas e lista , são imutáveis (conteúdo não pode ser modificado depois de criado)

# tuplas = (2,4,6,7,9)
# print(type(tuplas))

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5,5,6,7,8,9,4,6,5,7)
# # print(len(halogenios[3]))
# print(elementos)
# print(t1.count(3))

print(halogenios[0:2])  #slicing
print('Fe' in halogenios) 
print(sum(t1))  #min max 


# Operações não disponíveis em tuplas: .sort(), .append() , .reverse(), pop()
# todos que alteram, pois tupla é imutável



#ITERAÇÃO
for elemento in elementos:
    print(f'Elemento químico: {elemento}')


#CRIAR LISTA ATRAVÉS DE TUPLA 

grupo17 = list(halogenios)
print(grupo17)

# É POSSÍVEL O CONTRÁRIO

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)
print(alcalinos)

# NÃO DA PRA ALTERAR ORDEM DE ELEMENTOS, MAS DA PRA CRIAR UMA NOVA TUPLA

print(sorted(alcalinos)) #certo
print(alcalinos.sort()) #errado, só funciona em lista e outros objetos