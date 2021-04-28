from model.aritmetica_sumas import SumaAritmetica as sa


class GeneraSumas:

    def __init__(self, cantidad_sumas=1, sumandos=2, limite_inferior=0, limite_superior=10):
        self.cantidad_sumas = cantidad_sumas
        self.ejercicios = []
        for num_eje in range(self.cantidad_sumas):
            self.ejercicios.append(
                sa(sumandos=sumandos, limite_inferior=limite_inferior, limite_superior=limite_superior))

    def __str__(self):
        return 'Ejercicios : \n' + '\n'.join([ejer.__str__() for ejer in self.ejercicios])


if __name__ == '__main__':
    genera_sumas_service = GeneraSumas(cantidad_sumas=5, sumandos=5, limite_inferior=-100, limite_superior=100)
    print('Prueba servicio de generacion de sumas : {}'.format(genera_sumas_service.__str__()))
