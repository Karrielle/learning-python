#conjuntos ou sets, colução n ordenadas de valores unicos, nao duplicados suportam união, intersecção
# não consegue modificar items no set mas consegue adicionar novos elementos e consegue de qualquer tipo set é mutável
# planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'} #set só tem valores
# print(type(planeta_anao))
# print(len(planeta_anao))

#verificar se o conjunto tem ou não o valor 
# print('Ceres' in planeta_anao)
# print('Lua' in planeta_anao)
# # print('Lua' not in planeta_anao)

# # for astro in planeta_anao:
# #     print(astro.upper(), end='')

# astros = ['Lua', 'Vênus', 'Sirius', 'Marte', 'Lua']
# print(astros)
# astro_set = set(astros)
# print(astro_set)  #não tem valores duplicados


#COMPARAÇÕES ENTRE CONJUNTOS

astros1 = {'Lua', 'Vênus', 'Sirius', 'Marte','Io'}
astros2 = {'Lua', 'Vênus', 'Sirius', 'Marte', 'Cometa de Halley'}
# print(astros1 == astros2)
# print(astros1 != astros2)

# #UNIÃO DE CONJUNTOS
# print(astros1 | astros2)
# print(astros1.union(astros2))

# #INTERSECÇÃO, ELEMENTOS EM COMUM
# print(astros1 & astros2)
# print(astros1.intersection(astros2))

# #DIFERENÇA SIMÉTRICA
# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2))

#ADICIONAR ELEMENTOS A UM CONJUNTO

astros1.add('Urano')
astros1.add('Sol')
# astros1.remove('Io')
# astros1.remove('Plutão')  # da erro
# astros1.discard('Plutão')  # não da erro se não tiver
print(astros1) #ORDEM ALEATÓRIA


astros1.pop()  #remove arbitrariamente/aleatório bom pra jogos

astros1.clear()
print(astros1)


