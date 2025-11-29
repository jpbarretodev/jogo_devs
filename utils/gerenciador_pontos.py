# código feito exclusivamente para gerenciar os pontos
import json

caminho_combinacao = "utils/combinacoes_vencedoras.json"
caminho_pontos = "utils/multiplicador_pontos.json"

combinacoes_possiveis = []
pontuacoes = []

# abrir arquivos - combinacoes possíveis
with open(caminho_combinacao, "r") as file:
    combinacoes = json.load(file)

     # gerar lista de combinacoes
    for i in range(len(combinacoes)):
        combinacoes_possiveis.append(combinacoes["combinacao{}".format(i+1)])

with open(caminho_pontos, "r") as file:
    pontos = json.load(file)

    #gera lista dos pontos
    for i in range(len(pontos)):
        pontuacoes.append(pontos["combinacao{}".format(i+1)])

#################################################################################

def gerar_pontuacao(jogada_escolhida, saldo_inserido):
    if jogada_escolhida in combinacoes_possiveis:
        for indice, elemento in enumerate(combinacoes_possiveis):
            if jogada_escolhida == elemento:
                #return indice
                multiplicador_ponto = pontuacoes[indice]
                return saldo_inserido * multiplicador_ponto # retorna o saldo final do jogador na aposta

'''
print(combinacoes_possiveis)
print(pontuacoes)
#gerar_pontuacao([3, 3, 3], 5)
'''
