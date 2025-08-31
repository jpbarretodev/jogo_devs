# Classe exclusiva para a Máquina

import random # importação da biblioteca para realizar a randomização da escolha dos elementos
import json

caminho = "C:/Users/650B/Documents/jogo_devs/utils/combinacoes_vencedoras.json"

class Maquina:

    def __init__(self):
        self.jogada_vencedora = 0
        self.contador = 0
        self.combinacao_escolhida = [] # depois testar com 0
        self.saldo_inserido = 0 # para fins de teste de ganho/perda de saldo

    def zerar_maquina(self):
        self.contador = 0
        self.jogada_vencedora = 0
        self.combinacao_escolhida = []
        self.saldo_inserido = 0

    def gerar_jogada_perdedora(self):
        lista = [1, 2, 3]
        lista_nova = random.sample(lista, len(lista))
        #print(lista_nova)
        return lista_nova

    def gerar_jogada_vencedora(self):
        """
        Essa função gera a jogada em que o usuário vencerá a aposta
        """
        self.jogada_vencedora = random.randint(1, 4)
    
    def escolher_combinacao(self):
        """
        Essa função escolhe a combinação que o usuário receberá na jogada em que for vencedor
        """
        with open(caminho, "r") as file:
            combinacoes = json.load(file) # combinações agora é um dicionario em python
            combinacao = random.choice([combinacoes["combinacao1"], combinacoes["combinacao2"], combinacoes["combinacao3"]]) # escolhe a combinação
            self.combinacao_escolhida = combinacao

    def gerador_de_aposta(self): # combina as jogadas
        self.gerar_jogada_vencedora()
        self.escolher_combinacao()

    def jogada(self):
        #print(self.jogada_vencedora, self.combinacao_escolhida)
        self.gerador_de_aposta()

        while self.contador < self.jogada_vencedora:
            self.contador += 1
            self.gerar_jogada_perdedora()

        # jogada vencedora
        print("Jogador venceu!")
        self.zerar_maquina()

