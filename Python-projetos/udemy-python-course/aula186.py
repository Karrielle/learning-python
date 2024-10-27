import os


caminho_arquivo = 'C:\\Users\\mkarr\\Documents\\GitHub\\learning-python\\Python-projetos\\udemy-python-course\\'
caminho_arquivo += 'aula186.txt'

# arquivo = open(caminho_arquivo, 'w') 
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('LENDO')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())


# print('#' *10)


with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

os.unlink(caminho_arquivo) #remove #rename