# Classe exclusiva para a Máquina

import random # importação da biblioteca para realizar a randomização da escolha dos elementos
import json

caminho = "C:/Users/650B/Documents/jogo_devs/utils/combinacoes_vencedoras.json"

class Maquina:

    def __init__(self):
        self.jogada_vencedora = 0
        self.contador = 0
        self.combinacao_escolhida = [] # depois testar com 0

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

    def jogada(self, aposta_do_jogador):
        todas_combinacoes = []
        #print(self.jogada_vencedora, self.combinacao_escolhida)

        self.gerador_de_aposta() # aqui ja alterou a configuração da máquina


        while self.contador < self.jogada_vencedora:
            self.contador += 1
            aposta_do_jogador
            todas_combinacoes.append(self.gerar_jogada_perdedora())

        # jogada vencedora
        todas_combinacoes.append(self.combinacao_escolhida)
        #print("Lista: {}".format(todas_combinacoes))
        self.zerar_maquina()
        return todas_combinacoes
    
    def aposta(self, aposta_jogador):
        rodada = self.jogada(aposta_jogador)
        return rodada               # retorna a lista com as combinacoes perdedoras e a ganhadora por último. Chamar essa função no front, pfv não esquecer!

"""
m  = Maquina()
print(m.aposta())
"""