# Codigo exclusivo para testar a classe

from person.jogador import Jogador
from person.maquina import Maquina
from utils.gerenciador_pontos import gerar_pontuacao

# instanciando os objetos
m = Maquina()
user = Jogador("Tester", 100)

# primeiro passo do jogo: usuário insere o valor da aposta
user.apostar()

# segundo passo do jogo: maquina gera a jogada e retorna a lista para o front
lista = m.aposta(user.apostar()) # recebe TODA a jogada

# terceiro passo do jogo: precisa passar para o GERADOR DE PONTUAÇÃO a jogada e o saldo inserido
result = gerar_pontuacao(lista[len(lista) - 1], user.saldo_inserido)

# Quarto passo: alterar o saldo do usuário após aposta
user.saldo += result


# Verificar estado atual do jogador
print("Saldo atual: {}\nSaldo inserido: {}\nNovo saldo (valor aposta + multiplicador): {}".format(user.saldo, user.saldo_inserido, result))