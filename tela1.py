import pygame
import sys
import random

pygame.init()

# Config da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo de Telas")

#imagens
simbolos_imgs = [
    pygame.image.load("java.png"),
    pygame.image.load("javascript.png"),
    pygame.image.load("py.png")
]

simbolos_imgs = [
    pygame.transform.scale(img, (100, 100))
    for img in simbolos_imgs
]
imgs_atual=[
    random.choice(simbolos_imgs),
    random.choice(simbolos_imgs),
    random.choice(simbolos_imgs)
]

#painel
pygame.draw.rect(tela, (200, 0, 0), (80, 130, 450, 150), border_radius=20)   
pygame.draw.rect(tela, (255, 255, 0), (80, 130, 450, 150), 8, border_radius=20) 

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (50, 100, 255)

# Fonte
fonte = pygame.font.Font(None, 40)


tela_atual = "menu" 

def caixa_imgs(x, y, img):
    # fundo branco
    pygame.draw.rect(tela, (255, 255, 255), (x, y, 110, 110), border_radius=10)
    # borda preta
    pygame.draw.rect(tela, (0, 0, 0), (x, y, 110, 110), 5, border_radius=10)
    # imagem dentro com margem
    tela.blit(img, (x + 5, y + 5))

# Função para desenhar botão
def desenhar_botao(texto, x, y, largura, altura):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    # Verificar se o mouse está em cima do botão
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        cor = (150, 150, 255)
        if clique[0] == 1:
            return True
    else:
        cor = azul

    pygame.draw.rect(tela, cor, (x, y, largura, altura))
    texto_render = fonte.render(texto, True, preto)
    tela.blit(texto_render, (x + 10, y + 10))

    return False


# Loop principal
while True:
    tela.fill(branco)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #tela1
    if tela_atual == "menu":
        if desenhar_botao("Iniciar", 250, 300, 120, 60):
            tela_atual = "segunda"
            pygame.time.delay(200)

        texto1 = fonte.render("Bem vindo ao jogo!", True, preto)
        tela.blit(texto1, (200, 50))

    #tela2
    elif tela_atual == "segunda":
        texto2 = fonte.render("CAÇA-NÍQUEL", True, preto)
        tela.blit(texto2, (200,50))
        
        tela.blit(imgs_atual[0], (100, 150))
        tela.blit(imgs_atual[1], (250, 150))
        tela.blit(imgs_atual[2], (400, 150))
        
        caixa_imgs(100, 150, imgs_atual[0])
        caixa_imgs(250, 150, imgs_atual[1])
        caixa_imgs(400, 150, imgs_atual[2])
        
        if desenhar_botao("Girar", 250, 300, 120, 50):
            imgs_atual = [
            random.choice(imgs_atual),
            random.choice(imgs_atual),
            random.choice(imgs_atual)
        ]
            pygame.time.delay(200)
        if desenhar_botao("Voltar", 250, 350, 120, 50):
            tela_atual = "menu"
            pygame.time.delay(200)
            
    pygame.display.update()