# Exceção é um objeto que representa um erro que ocorreu ao executar o programa
# quando precisa tratar? quando suspeitamos que um trecho pode causar erro e se precaver de um erro explodir na cara do usuário 
# BLocos try ... except


def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print(f'Ocorreu um erro ao ler o valor. Tente novamente!')

    try:
        r = div(n1, n2)
    except ZeroDivisionError:
        print(f'Não é possível dividir por zero!')
    except:
        print(f'Ocorreu um erro desconhecido...')
    else:  
        print(f'Resultado: {r}')
    finally:                  #bloco de código associado que vai ser sempre executado indepentende se tem erro ou não
        print(f'\nFim do cálculo')


#FORÇAR LANÇAMENTO DE EXCEÇÃO, 





# try:   #código que suspeito
#     r = round(n1 / n2, 2)
# except ZeroDivisionError: # exceção, tratamento
#     print(f'Não é possível dividir por zero!')
# else:  #opcional, mas oq vai acontecer se nao tiver erro
#     print(f'Resultado: {r}')


