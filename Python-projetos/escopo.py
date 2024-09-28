# OQUE É?  INDICA A VISIBILIDADE DE UMA VAR DENTRO DO CÓDIGO E É ACESSÍVEL
#TEM ESCOPO GLOBAL E ESCOPO LOCAL

#LOCAL INICIADA TODA VEZ QUE A FUNÇÃO É CHAMADA, SOMENTE LOCAL DENTRO DA FUNÇÃO
# GLOBAL, CRIADA FORA DAS FUNÇÕES E PODE SER ACESSADA EM TODAS PARTES DO CÓDIGO,

#CUIDADO COM GLOBAIS

var_global = "Curso Completo de Python"

def escreve_texto():
    global var_global    #para alterar criada fora da função
    var_global = "Banco de Dados com SQL"
    var_local = "Fábi dos Reis"
    print(f'Variável Global: {var_global}')
    print(f'Variável Local: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variáveis diretamente')
    print(f'Variável Global: {var_global}')
   