# Orientação e Objetos: Paradigma de Programação
#Classes e Objetos  
# Classes são modelos abstratos que representam items do mundo real dentro do softwware
#Objetos são as ocorrencia dessas classes classes carregadas na memoria e existindo pra valer


#como representar pessoas, animais, conta  com poo

class Veiculo:     #atributos e metodos dentro, atributos são propriedades da classe, similar a variavel guardam valores. E métodos são as ações que a classe pode realizar ou sofrer, similares a função.
    def movimentar(self):
        print(f'Sou um veículo e me desloco!')   #self serve para falar que serve somente aquele objeto em particular

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro  = None             #__ emcapsulamento

    #Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter permite acessar atributos dentro da classe privados
    def get_fabr_modelo(self):
        print(f'Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n')
    
    def get_num_registro(self):
        return self.__num_registro
    

#herança     
class Carro(Veiculo):
    #Método __init_ será herdado
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas!')

class Motocicleta(Veiculo):
    def movimentar(self):
        print(f'Corro muito!')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat
    
    def movimentar(self):
        print(f'Eu voo alto!')
    

if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac Escalade')
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabr_modelo()
    # meu_veiculo.set_num_registro('490321-1')
    # print(f'Registro: {meu_veiculo.get_num_registro()}\n')


    # meu_carro = Carro('Volkswagen', 'Polo')
    # meu_carro.movimentar()
    # meu_carro.get_fabr_modelo()

    # seu_carro = Carro('Audi', 'A5 Sportback')
    # seu_carro.movimentar()
    # seu_carro.get_fabr_modelo

    # moto = Motocicleta('Harley-Davidson', 'Nightster Special')
    # moto.movimentar()
    # moto.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()
    print(f'Categoria: {meu_aviao.get_categoria()}')


#herança 



    



