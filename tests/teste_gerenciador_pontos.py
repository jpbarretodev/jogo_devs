from pathlib import Path
from utils.gerenciador_pontos import caminho_combinacao, caminho_pontos, gerar_pontuacao


# caminho absoluto (somente para o script de teste)
BASE = Path(__file__).resolve().parent.parent
CAMINHO_JSON1 = BASE / "utils" / "combinacoes_vencedoras.json"
CAMINHO_JSON2 = BASE / "utils" / "multiplicador_pontos.json"

caminho_combinacao = CAMINHO_JSON1
caminho

def testar_gerador_pontuacao(combinacao_vencedora = [3, 3, 3], saldo_aposta = 5):
	gerar_pontuacao(combinacao_vencedora, saldo_aposta)

testar_gerador_pontuacao()
