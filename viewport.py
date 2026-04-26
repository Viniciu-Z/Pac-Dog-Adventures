import pygame
from funcoes import *
import cachorro
import alimento
from cenario import MESAS, LARGURA_MESA, ALTURA_MESA

#cores
BRANCO = (255, 255, 255)
VERDE = (0, 150, 0)
VERMELHO = (200, 0, 0)
CINZA = (100, 100, 100)

#viewport (posição na tela)
VIEWPORT = (80, 520, 260, 640)

# Cachorro no Minimapa
def desenhar_cachorro_minimap(tela, m):
    metade = cachorro.TAMANHO // 2

    pontos = [
        (cachorro.x - metade, cachorro.y - metade),
        (cachorro.x + metade, cachorro.y - metade),
        (cachorro.x + metade, cachorro.y + metade),
        (cachorro.x - metade, cachorro.y + metade),
    ]

    pontos = aplica_transformacao(m, pontos)
    scanline_fill(tela, pontos, VERDE)
    desenhar_poligono(tela, pontos, BRANCO)

# Alimento no Minimapa
def desenhar_alimento_minimap(tela, m):
    r = alimento.TAMANHO_ALIMENTO // 2

    pontos = [
        (alimento.x - r, alimento.y - r),
        (alimento.x + r, alimento.y - r),
        (alimento.x + r, alimento.y + r),
        (alimento.x - r, alimento.y + r),
    ]

    pontos = aplica_transformacao(m, pontos)
    scanline_fill(tela, pontos, VERMELHO)

# Mesas no Minimapa
def desenhar_mesas_minimap(tela, m):
    for (mx, my) in MESAS:
        pontos = [
            (mx, my),
            (mx + LARGURA_MESA, my),
            (mx + LARGURA_MESA, my + ALTURA_MESA),
            (mx, my + ALTURA_MESA)
        ]

        pontos = aplica_transformacao(m, pontos)
        scanline_fill(tela, pontos, CINZA)

def desenhar_minimapa(tela, largura, altura):
    janela_mundo = (0, 0, largura, altura)

    m = janela_viewport(janela_mundo, VIEWPORT)

    # desenha elementos
    desenhar_mesas_minimap(tela, m)
    desenhar_alimento_minimap(tela, m)
    desenhar_cachorro_minimap(tela, m)

    # borda do minimapa
    x, y, x2, y2 = VIEWPORT
    pygame.draw.rect(
        tela,
        BRANCO,
        pygame.Rect(x, y, x2 - x, y2 - y),
        1
    )