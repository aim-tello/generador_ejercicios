import numpy as np
import random
from json import JSONEncoder


class RestaAritmetica:

    def __init__(self, sumandos=2, limite_inferior=0, limite_superior=10):
        self.sumandos = sumandos
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.vector_sumandos = np.random.randint(limite_inferior, limite_superior, size=sumandos)
        self.suma = self.calcula_suma()

    def calcula_suma(self):
        suma = '({})'.format(self.vector_sumandos[0])
        for sumando in self.vector_sumandos[1:]:
            if bool(random.getrandbits(1)):
                suma += '+'
            else:
                suma += '-'
            suma += '(' + str(sumando) + ')'
        suma += '='
        return suma

    def __str__(self):
        return self.suma


class RestaAritmeticaEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


if __name__ == '__main__':
    ejemplo_suma = RestaAritmetica()
    print('Ejemplo de suma sin argumentos :{}'.format(ejemplo_suma.__str__()))
    print(ejemplo_suma.vector_sumandos)
    ejemplo_suma2 = RestaAritmetica(limite_inferior=-100, limite_superior=100, sumandos=15)
    print('Ejemplo de suma con argumentos :{}'.format(ejemplo_suma2.__str__()))
    print(ejemplo_suma2.vector_sumandos)
    ejercicios = []
    for num_eje in range(5):
        ejercicios.append(
            RestaAritmetica(sumandos=5, limite_inferior=-1000, limite_superior=100))
    print('Ejercicios : \n' + '\n'.join([ejer.__str__() for ejer in ejercicios]))
