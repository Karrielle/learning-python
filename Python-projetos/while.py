# num = 1

# while (num <= 1000):
#     print(num)
#     num += 1  #atribuição + incremento
# print('Laço encerrado!')

nome = None

while True:
    print('Digite seu nome, ou x para parar:')
    nome = input()
    if nome == 'x' or nome == 'X':
        break
    print(f'Bem-vindo, {nome}')
print('Até logo!')
