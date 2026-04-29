import pygame
from funcoes import *

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)

LARGURA_MESA = 400
ALTURA_MESA = 235

MESAS = [
    (70, 70),
    (600, 70),
    (70, 410),
    (600, 410)
]

# Superfície pré-renderizada do cenário
cenario_surface = None

def desenhar_mesa(superficie, x, y):
    pontos = [
        (x, y),
        (x + LARGURA_MESA, y),
        (x + LARGURA_MESA, y + ALTURA_MESA),
        (x, y + ALTURA_MESA)
    ]

    janela = (0, 0, superficie.get_width(), superficie.get_height())

    scanline_fill(superficie, pontos, CINZA)
    desenhar_poligono_recortado(superficie, pontos, janela, PRETO)

def criar_cenario(largura, altura):
    global cenario_surface

    cenario_surface = pygame.Surface((largura, altura)).convert()
    cenario_surface.fill(BRANCO)

    for (x, y) in MESAS:
        desenhar_mesa(cenario_surface, x, y)

def desenhar_cenario(tela):
    tela.blit(cenario_surface, (0, 0))