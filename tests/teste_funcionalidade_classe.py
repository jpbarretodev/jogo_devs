# Codigo exclusivo para testar a classe

from person.jogador import Jogador
from person.maquina import Maquina
from utils.gerenciador_pontos import gerar_pontuacao

# instanciando os objetos
m = Maquina()
user = Jogador("Tester", 100)
perdeu = False

# primeiro passo do jogo: apostar o numero de vezes das jogadas

lista = m.aposta()
print(lista)

for i in range(len(lista)):

    user.apostar()

    if user.saldo <= 0 and i <= len(lista) - 2:
        print('Jogador perdeu sem ta na ultima rodada')
        perdeu = True
        break
    else:
        continue

if perdeu:
    print('burrao')
else:
    print('ganhou')