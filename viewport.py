import pygame
from funcoes import *
import cachorro
import alimento
from cenario import mesas, largura_mesa, altura_mesa

# cores
BRANCO = (255, 255, 255)
VERDE = (0, 150, 0)
VERMELHO = (200, 0, 0)
CINZA = (100, 100, 100)

# viewport (posição na tela)
viewport = (80, 520, 260, 640)

# Cachorro no Minimapa
def desenhar_cachorro_minimap(tela, m):
    metade = cachorro.tamanho // 2

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
    r = alimento.tamanho_alimento // 2

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
    for (mx, my) in mesas:
        pontos = [
            (mx, my),
            (mx + largura_mesa, my),
            (mx + largura_mesa, my + altura_mesa),
            (mx, my + altura_mesa)
        ]

        pontos = aplica_transformacao(m, pontos)
        scanline_fill(tela, pontos, CINZA)

def desenhar_borda_viewport(tela):
    x, y, x2, y2 = viewport

    pontos = [
        (x, y),
        (x2, y),
        (x2, y2),
        (x, y2)
    ]

    # desenha apenas a borda (sem fill)
    desenhar_poligono(tela, pontos, BRANCO)

def desenhar_minimapa(tela, largura, altura):
    janela_mundo = (0, 0, largura, altura)

    m = janela_viewport(janela_mundo, viewport)

    # desenha elementos
    desenhar_mesas_minimap(tela, m)
    desenhar_alimento_minimap(tela, m)
    desenhar_cachorro_minimap(tela, m)

    # borda do minimapa (sem pygame.draw)
    desenhar_borda_viewport(tela)