from model.aritmetica_restas import RestaAritmetica as ra


class GeneraRestas:

    def __init__(self, cantidad_restas=1, sumandos=2, limite_inferior=0, limite_superior=10):
        self.cantidad_restas = cantidad_restas
        self.ejercicios = []
        for num_eje in range(self.cantidad_restas):
            self.ejercicios.append(
                ra(sumandos=sumandos, limite_inferior=limite_inferior, limite_superior=limite_superior))

    def __str__(self):
        return 'Ejercicios : \n' + '\n'.join([ejer.__str__() for ejer in self.ejercicios])


if __name__ == '__main__':
    genera_restas_service = GeneraRestas(cantidad_restas=5, sumandos=5, limite_inferior=-100, limite_superior=100)
    print('Prueba servicio de generacion de sumas : {}'.format(genera_restas_service.__str__()))
