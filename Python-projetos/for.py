# lista  = [2,6,9,4,0,12,3,7]
# palavra = 'word'
# for letra in palavra:   #para cada item dentro da lista faça alguma coisa
#     print(letra)

# for numero in range(10):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

#range (valor_inicial, valor_final, incremento)

# for x in range(20,2,-2):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue #ao contrario do break o continue só pula o atual
    print(pedra)