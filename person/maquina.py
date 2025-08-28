# Classe exclusiva para a Máquina
import random                       # importação da biblioteca para realizar a randomização da escolha dos elementos


class Maquina:

    def __init__(self):
        pass

    @staticmethod
    def contador_de_jogadas():
        combinacao = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
        contador = 0
        while True:
            jogada = Maquina.gerar_combinacao()  # <-- chama a função a cada loop
            contador += 1
            if jogada in combinacao:
                break

        return print(contador)


    def realizar_aposta(saldo_de_aposta):
        pass

    @staticmethod
    def gerar_combinacao():
        lista = []
        for i in range(3):
            lista.append(random.randint(1, 3))
            #print(lista)
        return lista

Maquina.contador_de_jogadas()