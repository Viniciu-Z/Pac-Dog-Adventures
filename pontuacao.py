import pygame

PRETO = (0, 0, 0)

# Pontuação atual
pontos = 0

# Fonte (inicializada uma vez)
fonte = None

def iniciar():
    global fonte
    fonte = pygame.font.SysFont(None, 36)

def adicionar_ponto():
    global pontos
    pontos += 50

def resetar():
    global pontos
    pontos = 0

def desenhar(tela):
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    tela.blit(texto, (10, 10))