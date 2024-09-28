# nome = 'Curso de Python'
# instrutor =  'Matheus'
# letra = nome[2]
# print(letra)
# print(len(nome))
# print(nome + ' com ' + instrutor)

frase = 'Vamos aprender Python hoje.'
# palavras = frase.split()   #divide a string em partes, criando uma lista
# print(palavras[1])
# for palavra in palavras:
#     print(palavra)

# for letra in frase:
#     print(letra)

# print(frase[7:19])

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)


#IN OU NOT IN

# produtos = 'carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)
# print('magnésio' not in produtos)



#FINDD

# item = 'hipoclorito'
# pos = item.find('clor')
# print(pos)
# pos = item.find('flu')
# print(pos)



#PADRÃO DE LETRAS

# objeto_celeste = 'galáxia esPiral M31'  #usado pra padronizar login, por exemplo
# print(objeto_celeste.upper()) #tudo maiusculo
# print(objeto_celeste.lower()) #tudo minusculo
# print(objeto_celeste.capitalize()) #primeira letra maiuscula
# print(objeto_celeste.title())  #cada palavra a primeira letra fica maiuscula


# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')   #2 args, oq quero substituir, o valor que quero colocar
# print(suplemento)
# print(n_suplemento)


#eliminar espaços para tratar strings
# frase = '   ômega 3 é bom para a saúde!     '
# print(frase)
# print(frase.lstrip())
# print(frase.rstrip())
# print(frase.strip())



#ALINHAMENTO DE TEXTO PARA EXIBIÇÃO 
# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20))   #justificar a direita numero de caracteres pra usar 20 espaços e alinhado a direita
# print(fruta.center(20))
# print(fruta.ljust(20, "-"))  #util usando com o center, otimo para titulo de tabela menu

# print(fruta.center(20, "-"))


# p = 'Bóson Treinamentos'
# print(p.startswith('Bó'))  #começa com? sim ou não
# print(p.endswith('s'))  #termina com? sim ou não


#DOCSSTRINGS STRINGS LITERAIS PARA DOCUMENTAR TRECHO ESPECIFICO DO CODIGO, COMO FUNÇÃO, MODULOS

#use quando for criar modulos, funções, algo longo, do contrario comentário mesmo
texto = """
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função ou classe no Python, entre outros locais.
    Respeita deslocamento do texto e é    multilinhas
"""

print(texto)




