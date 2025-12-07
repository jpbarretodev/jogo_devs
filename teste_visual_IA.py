import pygame 
import random

# --- Classe Maquina (baseada no seu código) ---
class Maquina:
    def __init__(self):
        self.jogada_vencedora = 0
        self.contador = 0
        self.combinacao_escolhida = []

    def zerar_maquina(self):
        self.contador = 0
        self.jogada_vencedora = 0
        self.combinacao_escolhida = []

    def gerar_jogada_perdedora(self):
        return [random.randint(1,3) for _ in range(3)]

    def gerar_jogada_vencedora(self):
        self.jogada_vencedora = random.randint(2,5)  # mais de 1 para ver várias perdedoras

    def escolher_combinacao(self):
        combinacoes = {
            "combinacao1": [1,1,1],
            "combinacao2": [2,2,2],
            "combinacao3": [3,3,3]
        }
        self.combinacao_escolhida = random.choice(
            [combinacoes["combinacao1"], combinacoes["combinacao2"], combinacoes["combinacao3"]]
        )

    def gerador_de_aposta(self):
        self.gerar_jogada_vencedora()
        self.escolher_combinacao()

    def jogada(self):
        lista_combinacoes = []
        self.gerador_de_aposta()

        while self.contador < self.jogada_vencedora:
            self.contador += 1
            lista_combinacoes.append(self.gerar_jogada_perdedora())

        lista_combinacoes.append(self.combinacao_escolhida)  # jogada vencedora
        self.zerar_maquina()
        return lista_combinacoes

# --- Inicialização do Pygame ---
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Slot Machine Animada")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# --- Cores para cada número ---
cores = {1:(255,0,0), 2:(0,255,0), 3:(0,0,255)}

# --- Instancia a máquina ---
maquina = Maquina()
todas_jogadas = maquina.jogada()  # lista de jogadas

# --- Função para desenhar uma jogada ---
def desenhar_jogada(jogada, mensagem):
    screen.fill((0,0,0))
    x = 100
    for numero in jogada:
        pygame.draw.rect(screen, cores[numero], (x,150,80,80))
        texto = font.render(str(numero), True, (255,255,255))
        screen.blit(texto, (x+25,170))
        x += 120
    msg = font.render(mensagem, True, (255,255,0))
    screen.blit(msg, (120,50))
    pygame.display.flip()

# --- Loop para animar cada jogada ---
for idx, jogada in enumerate(todas_jogadas):
    mensagem = "Jogada perdedora" if idx < len(todas_jogadas)-1 else "Jogada vencedora!"
    animacao = 10  # número de ciclos de rolagem

    # Animação: gira os números antes de parar
    for _ in range(animacao):
        temp_jogada = [random.randint(1,3) for _ in range(3)]
        desenhar_jogada(temp_jogada, mensagem)
        pygame.time.delay(100)  # velocidade da rolagem

    # Mostra a jogada real depois da rolagem
    desenhar_jogada(jogada, mensagem)
    pygame.time.delay(800)  # pausa final antes da próxima jogada

pygame.time.delay(2000)
pygame.quit()
