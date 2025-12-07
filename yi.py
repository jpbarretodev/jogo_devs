import pygame
import random
import sys

pygame.init()

# Tela
largura, altura =800,400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caça Níquel")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Fonte
FONTE = pygame.font.SysFont("Arial", 24)

# Rolos
largura_rolo = 100
altura_rolo = 100
num_rolos = 3

posicao_x = [150, 250, 350]
posicao_y = [100] * num_rolos

pygame.init()

# Criar tela
tela = pygame.display.set_mode((800, 300))
pygame.display.set_caption("Imagens lado a lado")

# Carregar imagens (corrigido)
simbolos_imgs = [
    pygame.image.load("java.png"),
    pygame.image.load("javascript.png"),
    pygame.image.load("py.png")
]

# Redimensionar imagens (opcional)
simbolos_imgs = [
    pygame.transform.scale(img, (200, 200))
    for img in simbolos_imgs
]

# Posições das 3 imagens
posicoes = [
    (50, 50),   # imagem 1
    (300, 50),  # imagem 2
    (550, 50)   # imagem 3
]

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))  # fundo branco

    # Desenhar as imagens na tela
    for img, pos in zip(simbolos_imgs, posicoes):
        tela.blit(img, pos)

    pygame.display.update()

pygame.quit()

simbolos = [random.randint(0, len(simbolos_imgs) - 1) for _ in range(num_rolos)]

# Botão
botao_girar = pygame.Rect(largura//2 - 50, 300, 100, 40)

# Animação
girando = False
tempo_giro = 0
duracao_giro = 60

def desenhar_rolos():
    for i in range(num_rolos):
        tela.blit(simbolos_imgs[simbolos[i]], (posicao_x[i], posicao_y[i]))
        pygame.draw.rect(tela, branco, (posicao_x[i], posicao_y[i], largura_rolo, altura_rolo), 3)

def desenhar_botao():
    pygame.draw.rect(tela, (100, 100, 100), botao_girar)
    texto = FONTE.render("Girar", True, branco)
    tela.blit(texto, (botao_girar.x + 20, botao_girar.y + 10))

def atualizar_rolos():
    global simbolos
    for i in range(num_rolos):
        simbolos[i] = random.randint(0, len(simbolos_imgs) - 1)

def main():
    global girando, tempo_giro
    
    relogio = pygame.time.Clock()
    rodando = True

    while rodando:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_girar.collidepoint(evento.pos) and not girando:
                    girando = True
                    tempo_giro = duracao_giro

        if girando:
            if tempo_giro > 0:
                atualizar_rolos()
                tempo_giro -= 1
            else:
                girando = False

        desenhar_rolos()
        desenhar_botao()

        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()
    sys.exit()

    return main()