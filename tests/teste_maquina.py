# Codigo exclusivo para testar a classe da máquina

from person.maquina import Maquina
from utils.gerenciador_pontos import gerar_pontuacao
from pathlib import Path

# caminho absoluto (somente para o script de teste)
BASE = Path(__file__).resolve().parent.parent
CAMINHO_JSON = BASE / "utils" / "combinacoes_vencedoras.json" 

# instanciando os objetos
maquina = Maquina()

def teste_gerar_jogada_perdedora(numero_de_geracoes):
	for i in range(numero_de_geracoes):
		print("id das imagens: {}\n".format(maquina.gerar_jogada_perdedora()))
		
def teste_gerar_jogada_vencedora(numero_de_geracoes):
	for i in range(numero_de_geracoes):
		print("Vence na aposta de número {}\n".format(maquina.gerar_jogada_vencedora()))

def teste_escolher_combinacao(numero_de_escolhas):
	for i in range(numero_de_escolhas):
		print("combinação no momento {}: {}\n".format(i+1, maquina.escolher_combinacao(CAMINHO_JSON)))
		
def teste_montar_jogada(numero_de_jogadas, dir_caminho = CAMINHO_JSON):
	for i in range(numero_de_jogadas):
		print("Jogada na aposta {}: {}\n".format(i+1, maquina.jogada(dir_caminho)))
		